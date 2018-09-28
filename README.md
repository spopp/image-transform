# Python Image Processing


## Linux Setup

./setup.sh - sets up the Python3 virtual environment in the venv folder and installs the Pillow image library

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

```
deactivate
```


