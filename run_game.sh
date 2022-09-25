#!/bin/bash
echo "Hello! Thank you for downloading this terminal application."
cd ./src;
if [[ -x "$(command -v python3)" ]]
then
    pyv="$(python3 -V 2>&1)"
    if [[ $pyv == "Python 3"* ]]
    then
        echo "You have the correct version of python installed."
    else
        echo "You have an outdated version of python" >&2
        sudo add-apt-repository ppa:deadsnakes/ppa
        sudo apt-get update
        sudo apt-get install python3.9 python3-pip
    fi 
else
    echo "You don't have python, go get it!" >&2
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