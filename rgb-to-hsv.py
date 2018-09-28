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
        #  Get R plane, G plane, and B plane ima#

        # Remove the Apha Transparency Channel by using underscore
        red, green, blue, _ = img.split()

        #  Place Holder for HSV data
        Hdat = []
        Sdat = []
        Vdat = []

        for rd, gn, bl in zip(red.getdata(), green.getdata(), blue.getdata()):

            # Get raw H S V Plane data
            h, s, v = colorsys.rgb_to_hsv(rd/255., gn/255., bl/255.)

            Hdat.append(int(h*255.))
            Sdat.append(int(s*255.))
            Vdat.append(int(v*255.))
            #  Note: if you left out *255 above you have
            # 0 to 1 decimal values in Vdat

        # Now convert the HSV data back into an new RGB Image
        # without Alpha Channel placing hsv data into rgb planes
        red.putdata(Hdat)
        green.putdata(Sdat)
        blue.putdata(Vdat)

        return Image.merge('RGB', (red,  green,  blue))
    else:
        return None


def main():
    print('Reading image file images/test.jpg')
    image_rgb = Image.open('images/test.jpg')
    image_hsv = HSVColor(image_rgb)

    if image_hsv:
        # Save HSV image without alpha channel
        print('writing image file images/result.jpg')
        image_hsv.save('images/result.jpg')

if __name__ == '__main__':
    main()
