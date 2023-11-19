#!/bin/bash

app="$1"
venv="${app//app/venv}"
venv="${venv%.py}"

XVENV="$VIRTUAL_ENV"
XPATH="$PATH"

source "$venv/bin/activate"
python3 "$app"
deactivate

PATH="$XPATH"
VIRTUAL_ENV="$XVENV"

if [[ -z "$VIRTUAL_ENV" ]]
then
	source "$VIRTUAL_ENV/bin/activate"
fi
