#!/usr/bin/env bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

source $SCRIPT_DIR/setup_example_project.sh example_change_submodules_git_protocol

kicad_utils submodules set_protocol https
cat $EXAMPLE_DIR/.gitmodules

kicad_utils submodules set_protocol ssh
cat $EXAMPLE_DIR/.gitmodules

