#!/usr/bin/env python3
"""
Purpose:
  To convert RGB to to multi-value HSV and plot the spectrum image

Ideas From:
  https://github.com/msolters/rainbow-vision/blob/master/visualize-colors.py

Usage:
  cd  image-transform
  source bashrc

  ./rgbspectrum.py -f images/test.jpg
  or
  python3 rgbspectrum.py --filename images/test.jpg --outfile out/spectrum.jpg

"""

import argparse
import colorsys

from matplotlib import pyplot as plot
from mpl_toolkits.mplot3d.axes3d import Axes3D
from PIL import Image


def rgb_spectrum(img, outfile=None, mono=False):

    """
    Create a multi-valued HSV Spectrum from an RGB

    Parameters:
    img - an opem image file of type PIL Image.Image
    outfile - optional output file name for saving the spectrial image produced

    Return:
    matplotlib.pyplot Object
    """
    if isinstance(img, Image.Image):
        # (2) Construct a blank matrix representing the pixels in the image
        print('Processing the image')
        print(img.mode)
        xs, ys = img.size
        max_intensity = 100
        hues = {}
        pixel_access = img.load()

        # (3) Examine each pixel in the image file
        for x in range(0, xs):
            for y in range(0, ys):
                # ( )  Get the RGB color of the pixels
                try:
                    [r, g, b, _] = pixel_access[x, y]
                except ValueError:
                    [r, g, b] = pixel_access[x, y]

                # ( )  Normalize pixel color values
                if mono:
                    single = max(r, g, b)
                    r = single / 255.0
                    g = single / 255.0
                    b = single / 255.0
                else:
                    r /= 255.0
                    g /= 255.0
                    b /= 255.0

                # ( )  Convert RGB color to HSV
                [h, s, v] = colorsys.rgb_to_hsv(r, g, b)

                if h not in hues:
                    hues[h] = {}
                if v not in hues[h]:
                    hues[h][v] = 1
                else:
                    if hues[h][v] < max_intensity:
                        hues[h][v] += 1

        # ( )   Decompose the hues tree into a set of dimensional arrays
        h_ = []
        v_ = []
        i = []
        colours = []

        for h in hues:
            for v in hues[h]:
                h_.append(h)
                v_.append(v)
                i.append(hues[h][v])
                [r, g, b] = colorsys.hsv_to_rgb(h, 1, v)
                colours.append([r, g, b])

        # ( )   Plot the graph!
        fig, ax = plot.subplots()

        if not mono:
            ax = Axes3D(fig)
            ax.scatter(h_, v_, i, s=5, c=colours, lw=0)
            ax.set_xlabel('Hue')
            ax.set_ylabel('Value')
            ax.set_zlabel('Intensity')
            ax.set_title('Multi-valued Spectrum')
        else:
            ax.scatter(v_, i, s=5, c=colours, lw=0)
            ax.set_xlabel('Value')
            ax.set_ylabel('Intensity')
            ax.set_title('Single-valued Spectrum')

        if outfile is not None:
            print('Saving spectral image to {}'.format(outfile))
            fig.savefig(fname=outfile, pad_inches=0.5)

        return plot


def main():
    parser = argparse.ArgumentParser('Image file spectrial analysis')
    parser.add_argument('-f', '--filename', required=True,
                        help='Image file to read')
    parser.add_argument('-o', '--outfile', required=False,
                        help='Image file to write')
    parser.add_argument('-m', '--mono', action='store_true', required=False,
                        help='Generate a monochrome spectrum')
    args = parser.parse_args()

    print('Reading image file {}'.format(args.filename))
    # (1) Import the file to be analyzed
    image_file = Image.open(args.filename)

    plot = rgb_spectrum(image_file, outfile=args.outfile, mono=args.mono)

    plot.show()


if __name__ == '__main__':
    main()
