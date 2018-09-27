
sudo apt update
sudo apt install python3-venv

sudo pip install virtualenv --upgrade

# Setup a python3 virtual environment
[[ -d .env ]] || virtualenv venv -p python3  --no-site-packages


# Use the virtual environment
source ./bashrc

pip install Pillow

# Get out if the virtual environment
deactivate
