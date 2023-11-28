#!/usr/bin/env bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )


if [ -e $SCRIPT_DIR/~template_project_kicad.kicad_pcb.lck ] || [ -e $SCRIPT_DIR/~template_project_kicad.kicad_sch.lck ]; then
    echo "KiCad seems to be running and the schematic or pcb is open. Please close both an run the script again!"
    exit -1
fi



if [ $# -eq 0 ]; then
    echo "New projects name: "
    read NEW_PROJECT_NAME
else
    NEW_PROJECT_NAME=$1
fi


echo Init project \"$NEW_PROJECT_NAME\


set -x

mv $SCRIPT_DIR/template_project_kicad.kicad_pro $SCRIPT_DIR/$NEW_PROJECT_NAME.kicad_pro
mv $SCRIPT_DIR/template_project_kicad.kicad_prl $SCRIPT_DIR/$NEW_PROJECT_NAME.kicad_prl
mv $SCRIPT_DIR/template_project_kicad.kicad_sch $SCRIPT_DIR/$NEW_PROJECT_NAME.kicad_sch
mv $SCRIPT_DIR/template_project_kicad.kicad_pcb $SCRIPT_DIR/$NEW_PROJECT_NAME.kicad_pcb
