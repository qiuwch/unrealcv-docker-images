#!/bin/bash
# project_folder=$1
if [ -z ${project_folder} ]; then
  echo Please specify project folder
else
  echo Project folder is ${project_folder}
  rm -rf ${project_folder}/Plugins
  mkdir ${project_folder}/Plugins
  cp -r ${plugin_folder} ${project_folder}/Plugins/unrealcv
fi
