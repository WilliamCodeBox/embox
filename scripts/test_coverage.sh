#!/bin/bash

# This script can run anywhere

# Determine script absolute path
SCRIPT_ABS_PATH=$(readlink -f ${BASH_SOURCE[0]})
SCRIPT_ABS_PATH=$(dirname ${SCRIPT_ABS_PATH})

# switch to root folder
ROOT=$(readlink -f ${SCRIPT_ABS_PATH}/../)
cd $ROOT

coverage run --source empy -m pytest
coverage report -m