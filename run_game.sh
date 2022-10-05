#!/bin/bash
echo "Hello! Thank you for downloading this terminal application."
cd ./src;
if [[ -x "$(command -v python3)" ]]
then
    pyv="$(python3 -V 2>&1)"
    if [[ $pyv == "Python 3"* ]]
    then
        echo "You have the correct version of Python installed."
    else
        echo "You have an outdated version of Python. Please update Python." >&2
        
    fi 
else
    echo "You don't have Python, please install it to run the application!" >&2
fi
echo "First I will create a virtual environment using the standard name .venv"
python3 -m venv .venv 
echo "Next I will activate the virtual environment"
source .venv/bin/activate
echo "Now I will install all of the dependencies of the application"
pip install -r ./requirements.txt
echo "Now we can run the python file"
python3 ./main.py
deactivate