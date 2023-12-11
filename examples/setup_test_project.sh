#!/usr/bin/env bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

EXAMPLE_NAME=$1

mkdir -p $SCRIPT_DIR/data/
rm -f -r $SCRIPT_DIR/data/$EXAMPLE_NAME

python -m venv venv
source venv/bin/activate

pip install $SCRIPT_DIR/..

git clone https://github.com/twyleg/template_project_kicad.git $SCRIPT_DIR/data/$EXAMPLE_NAME

cd $SCRIPT_DIR/data/$EXAMPLE_NAME
git submodule update --init
