#!/bin/bash

bas=$(dirname $(readlink -f $0))

which python3 || {
	echo "Python3 not found :(";
	exit 1;
}

if [[ "$1" == "reinit" ]]
then
	rm -rf "$bas/venv1"
	rm -rf "$bas/venv2"
	rm -rf "$bas/venv3"
fi

if [[ ! -d "$bas/venv1" ]] 
then
	python3 -m venv "$bas/venv1"
	source "$bas/venv1/bin/activate"
	python3 -m pip install termcolor
	deactivate	
fi

if [[ ! -d "$bas/venv2" ]]
then
	python3 -m venv "$bas/venv2"
	source "$bas/venv2/bin/activate"
	python3 -m pip install rich
	deactivate
fi

if [[ ! -d "$bas/venv3" ]]
then
	python3 -m venv "$bas/venv3"
	source "$bas/venv3/bin/activate"
	python3 -m pip install cowsay
	deactivate
fi
