# Python Image Processing


## Linux 

./setup.sh - sets up the Python3 virtual environment in the venv folder and installs the Pillow image library
Some of the libraries had to be setup as a System Python3 package such as matplotlib.


## Virtual environment background information

Virtual environments are optional but I use them to keep my machines python libraries clean. If you use a virtual environment you will need to activate the environment by sourcing the bashrc script. Then use the environment by executing python scripts.  After use the deactivate command to deactivate the virtualenvironment if you want to keep using the terminal outside the environment.

## Activate the python3 virtual environment

This makes a python3 virtual environment active in a terminal window.
The full python3 virtual environment is contained in the .env folder which contains the Pillow library.

```bash
source bashrc

./rgb-to-hsv.py
```

Produces images/result.jpg - which you can delete

* the resulting image is not quite right
* When I split the image I do not get just RGB - we get a 4th plane that may be the alpha plane.

## Deactivate the python3 virtual environment

```bash
deactivate
```

## Information Sources

* https://iiw.kuleuven.be/onderzoek/eavise/mastertheses/billiauwsbonjean.pdf
* https://pillow.readthedocs.io/en/5.2.x/
* http://www.spectralpython.net/ - Rquires Python 2.7
* https://github.com/imagej/imagej.py Can run on Android - Requires Python 2.7, Java, Pyjnius, and imglib2-imglyb
* https://sydney.edu.au/medicine/bosch/facilities/advanced-microscopy/user-support/ImageJ_FL_Image_Analysis.pdf
* https://github.com/msolters/rainbow-vision/blob/master/visualize-colors.py - a hsv spectrum solution


## Choices

I would prefer to use one programming language though more may be needed depending on the choices made

* ImageJ is written in Java, and can run on Android.  imagej.py is written in python and requires python 2, not 3
* spectralpython requires python 2, not 3im
* Scikit-image - scipy - compatible with python 3


## Files

|  *File*               | *Purpose*             | *Notes*                       |
|-----------------------|-----------------------|-------------------------------|
| bashrc                | Activate virtualenv   | source bashrc to enter virtual environment, deactivate to leave |
| setup.sh              | Virtualenv and python packages | done one-time |
| requirements.txt      | Python packages to install | using pip |
| rgb.-to-hsv.py        | RGB to HSV and back   | Does not work correctly |
| rgbspectrum.py        | Spectrial analysis of image | Multi-Value Spectrum - works well |


## Matplot backends
Matplot may use several different backend modules for displaying imanges

| GTKAgg | Agg rendering to a GTK 2.x canvas (requires PyGTK and pycairo or cairocffi; Python2 only) |
| GTK3Agg | Agg rendering to a GTK 3.x canvas (requires PyGObject and pycairo or cairocffi) |
| GTK | GDK rendering to a GTK 2.x canvas (not recommended and d eprecated in 2.0) (requires PyGTK and pycairo or cairocffi; Python2 only) |
| GTKCairo | Cairo rendering to a GTK 2.x canvas (requires PyGTK and pycairo or cairocffi; Python2 only) |
| GTK3Cairo	| Cairo rendering to a GTK 3.x canvas (requires PyGObject and pycairo or cairocffi) |
| WXAgg| Agg rendering to to a wxWidgets canvas (requires wxPython) |
| WX | Native wxWidgets drawing to a wxWidgets Canvas (not recommended and deprecated in 2.0) (requires wxPython) |
| TkAgg | Agg rendering to a Tk canvas (requires TkInter) |
| Qt4Agg | Agg rendering to a Qt4 canvas (requires PyQt4 or pyside) |
| Qt5Agg | Agg rendering in a Qt5 canvas (requires PyQt5) |
| macosx | Cocoa rendering in OSX windows (presently lacks blocking show() behavior when matplotlib is in non-interactive mode) |
