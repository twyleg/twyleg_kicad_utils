#!/usr/bin/env bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

function setup_python () {
  python -m venv venv
  source venv/bin/activate
  pip install $SCRIPT_DIR/..
}

function setup_template_project_kicad () {
  if [ ! -d "$SCRIPT_DIR/data/template_project_kicad" ]; then
    git clone https://github.com/twyleg/template_project_kicad.git $SCRIPT_DIR/data/template_project_kicad
  else
    cd $SCRIPT_DIR/data/template_project_kicad
    if [ ! -z "$(git status --porcelain)" ]; then
      echo -e "\033[0;31;5m-- Caution: Changes in template_project_kicad --\033[0;0m"
    else
      echo -e "\033[0;32mtemplate_project_kicad is clean\033[0;0m"
    fi
  fi
}

EXAMPLE_NAME=$1

TEMPLATE_DIR=$SCRIPT_DIR/data/template_project_kicad
EXAMPLE_DIR=$SCRIPT_DIR/data/$EXAMPLE_NAME

mkdir -p $SCRIPT_DIR/data/
rm -rf $EXAMPLE_DIR

setup_python
setup_template_project_kicad

cp -r $TEMPLATE_DIR $EXAMPLE_DIR

cd $EXAMPLE_DIR
