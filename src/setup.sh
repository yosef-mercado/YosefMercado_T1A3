#!/bin/bash

if ! [[ -x "$(command -v python3)" ]]
then
    echo 'Error: 
        This program runs on Python 3, but it looks like Python 3 is not installed.
        To install Python 3, go to https://installpython3.com/' >&2
    exit 1
else
    if ! [[ -x "$(command -v pip)" ]]
    then
        echo 'Error: 
            This program requires the installation of Python modules from PyPI using pip.
            To install pip, go to https://pip.pypa.io/en/stable/installation/' >&2
        exit 1
    fi
fi

python3 -m pip install aenum
python3 -m pip install dice