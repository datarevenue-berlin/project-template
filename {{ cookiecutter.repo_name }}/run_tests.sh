#!/bin/bash

# SETUP ARTIFACTS ON CIRCLECI
DEFAULT_PATH=`pwd`/reports
CIRCLE_ARTIFACTS=${CIRCLE_ARTIFACTS:-$DEFAULT_PATH}
mkdir -p $CIRCLE_ARTIFACTS
echo wirting coverage report to $CIRCLE_ARTIFACTS

# EXPORT MODULE TO PYTHONPATH
export PYTHON_PATH=`pwd`:$PYTHON_PATH
export DRTOOLS_SETTINGS_MODULE={{ cookiecutter.repo_name }}.settings.settings

# RUN TESTS AND CREATE REPORTS
py.test {{ cookiecutter.repo_name }}