#!/bin/bash

app="$1"
venv="${app//app/venv}"
venv="${venv%.py}"

source "$venv/bin/activate"
python3 "$app"
deactivate
