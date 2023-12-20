#!/usr/bin/env bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

source $SCRIPT_DIR/setup_example_project.sh example_diff

git submodule update --init
kicad_utils diff -c -p 8181
