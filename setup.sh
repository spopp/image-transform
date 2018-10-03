

if [ virtualenv does not exist ]; then
   echo "Install virtualenv."
   sudo apt update
   sudo apt install libffi-dev libffi6 libcairo2-dev cairo

   # This had to be installed in the system not in virtualenv
   sudo pip install pycairo
   sudo apt install python3-venv
   sudo pip install virtualenv --upgrade
fi


# Setup a python3 virtual environment
[[ -d .env ]] || virtualenv venv -p python3


# Use the virtual environment
source ./bashrc

# Install required python packages
pip install -r requirements.txt

# Get out if the virtual environment
deactivate
