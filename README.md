# Share Scraper

## Installation
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
    # Create a config file to store your scraper-api key
    cp app.cfg.template app.cfg
    ```
    In ```app.cfg```, replace ```your-key-here``` with your own scraper-api key.

1. Run the project

    ```bash
    ./run-server.sh
    ```
