#!/usr/bin/env bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

EXAMPLE_NAME=example_change_submodules_git_protocol
$SCRIPT_DIR/setup_test_project.sh $EXAMPLE_NAME
source venv/bin/activate

cd $SCRIPT_DIR/data/$EXAMPLE_NAME

kicad_utils submodules --http
