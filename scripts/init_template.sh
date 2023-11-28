#!/usr/bin/env bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )


if [ $# -eq 0 ]; then
    echo "New projects name: "
    read NEW_PROJECT_NAME
else
    NEW_PROJECT_NAME=$1
fi


echo Init project \"$NEW_PROJECT_NAME\


# template_project_kicad.kicad_pcb
# -rw------- 1 twyleg twyleg   52 28. Nov 02:11 '~template_project_kicad.kicad_pcb.lck'
# -rw------- 1 twyleg twyleg 1.2K 27. Nov 22:12  template_project_kicad.kicad_prl
# -rw------- 1 twyleg twyleg  12K 27. Nov 22:12  template_project_kicad.kicad_pro
# -rw------- 1 twyleg twyleg  13K 28. Nov 02:06  template_project_kicad.kicad_sch

set -x

mv $SCRIPT_DIR/template_project_kicad.kicad_pro $SCRIPT_DIR/$NEW_PROJECT_NAME.kicad_pro
mv $SCRIPT_DIR/template_project_kicad.kicad_prl $SCRIPT_DIR/$NEW_PROJECT_NAME.kicad_prl
mv $SCRIPT_DIR/template_project_kicad.kicad_sch $SCRIPT_DIR/$NEW_PROJECT_NAME.kicad_sch
mv $SCRIPT_DIR/template_project_kicad.kicad_pcb $SCRIPT_DIR/$NEW_PROJECT_NAME.kicad_pcb
