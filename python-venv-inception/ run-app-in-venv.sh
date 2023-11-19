#!/bin/bash

if [[ "$1" == "-h" || "$1" == "--help" ]]
then
	echo "Usage"
	echo "First activate a given virtual env,"
	echo "Second execute python application,"
	echo "Third using given wrapper."
	echo "$(basename $0) <application_number> <venv_number <wrapper_number>"
	echo "$(basename $0) 1 2 3 # app1.py venv2 wrapper3.sh"
	exit 0
fi

bas="$(dirname $(readlink -f $0))"
app="$bas/app${1}.py"
venv="$bas/venv${2}"
wrapper="$bas/wrapper${3}.sh"

if [[ ! -f "$app" ]]
then
	echo "$app not found"
	exit 1
fi

if [[ ! -f "$venv/bin/activate" ]]
then
	echo "$venv not venv"
	exit 2
fi	

if [[ ! -f "$wrapper" ]]
then
	echo "Wrapper $wrapper not found"
	exit 3
fi

source "$venv/bin/activate"
pre_env="$(env)"
"$wrapper" "$app"
echo ""
post_env="$(env)"
deactivate

echo "Is there a change?"
diff <(echo "$pre_env") <(echo "$post_env")
