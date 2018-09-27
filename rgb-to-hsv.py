#!/usr/bin/env python
"""
Purpose:
  To test the Pillow Image Processing Library

Usage:
  cd  image-transform
  source bashrc

  ./rgbb-to-hsv.py
"""

import colorsys
from PIL import Image


def HSVColor(img):

    if isinstance(img, Image.Image):
        #  Get R plane, G plane, and B plane image data
        r, g, b, a = img.split()

        #  Place Holder for HSV data
        Hdat = []
        Sdat = []
        Vdat = []

        for rd, gn, bl in zip(r.getdata(), g.getdata(), b.getdata()):

            # Get raw H S V Plane data
            h, s, v = colorsys.rgb_to_hsv(rd/255., gn/255., bl/255.)

            Hdat.append(int(h*255.))
            Sdat.append(int(s*255.))
            Vdat.append(int(v*255.))
            #  Note: if you left out *255 above you have
            # 0 to 1 decimal values in Vdat

        # Now convert the HSV data into an new RGB Image
        r.putdata(Hdat)
        g.putdata(Sdat)
        b.putdata(Vdat)

        return Image.merge('RGB', (r,  g,  b))
    else:
        return None


def main():
    image_rgb = Image.open('images/test.jpg')
    image_hsv = HSVColor(image_rgb)

    if image_hsv:
        image_hsv.save('images/result.jpg')


if __name__ == '__main__':
    main()
