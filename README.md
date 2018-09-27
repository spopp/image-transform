# Python Image Processing


## Linux Setup

./setup.sh - sets up the Python3 virtual environment in the .env and installs Pillow


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

```
deactivate
```


