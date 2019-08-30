#Share Scraper#

##Installation##
1. Clone this project.
1. Install Python 3.7 and `pip` for Python 3.7:

    ```bash
    # Ensure you have python3.7 installed:
    sudo apt update && sudo apt install python3.7
    # Install pip for python3 (currently this is points to python3.6)
    sudo apt install python3-pip
    # Now install pip for python3.7
    python3.7 -m pip install pip
    ```
1. Install the [Gecko driver](https://github.com/mozilla/geckodriver) on your server
by running the following [instructions](https://askubuntu.com/a/863211) (for Ubuntu):

    ```bash
    export GECKO_DRIVER_VERSION='v0.24.0'
    wget https://github.com/mozilla/geckodriver/releases/download/$GECKO_DRIVER_VERSION/geckodriver-$GECKO_DRIVER_VERSION-linux64.tar.gz
    tar -xvzf geckodriver-$GECKO_DRIVER_VERSION-linux64.tar.gz
    rm geckodriver-$GECKO_DRIVER_VERSION-linux64.tar.gz
    chmod +x geckodriver
    sudo cp geckodriver /usr/local/bin/
    rm geckodriver

    ```
1. Install the project's dependencies (instructions for Ubuntu):

    ```bash
    # Replace $PROJECT_ROOT with the root directory of the cloned project
    cd $PROJECT_ROOT
    # Install the virtualenv package with pip
    python3.7 -m pip install virtualenv
    # Create a virtual environment for the project
    python3.7 -m virtualenv env
    # Activate the virtual environment
    source ./env/bin/activate
    # Install the project's requirements
    python3.7 -m pip install -r requirements.txt
    ```

