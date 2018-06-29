#!/bin/bash

project_folder="/Users/zimin/Desktop/KTH/Master-Thesis/projects"
script_folder="/Users/zimin/Desktop/KTH/Master-Thesis/defects4j-repair-runner"

if [ $# -eq 1 ]; then
  if [ "$1" = "Math" ]; then
    cd $project_folder
    mkdir $(echo "$1" | tr '[:upper:]' '[:lower:]')
    for id in {1..106}
    do
      cd ${project_folder}/$(echo "$1" | tr '[:upper:]' '[:lower:]')
      mkdir $(echo "$1" | tr '[:upper:]' '[:lower:]')_$id
      cd $(echo "$1" | tr '[:upper:]' '[:lower:]')_$id
      defects4j checkout -p $1 -v ${id}b -w ./
      cd $script_folder
      python defects4j-g5k-node.py -project $1 -tool Genprog -id $id
    done
  elif [ "$1" = "Chart" ]; then
    cd $project_folder
    mkdir $(echo "$1" | tr '[:upper:]' '[:lower:]')
    for id in {1..26}
    do
      cd ${project_folder}/$(echo "$1" | tr '[:upper:]' '[:lower:]')
      mkdir $(echo "$1" | tr '[:upper:]' '[:lower:]')_$id
      cd $(echo "$1" | tr '[:upper:]' '[:lower:]')_$id
      defects4j checkout -p $1 -v ${id}b -w ./
      cd $script_folder
      python defects4j-g5k-node.py -project $1 -tool Genprog -id $id
    done
  elif [ "$1" = "Closure" ]; then
    cd $project_folder
    mkdir $(echo "$1" | tr '[:upper:]' '[:lower:]')
    for id in {1..133}
    do
      cd ${project_folder}/$(echo "$1" | tr '[:upper:]' '[:lower:]')
      mkdir $(echo "$1" | tr '[:upper:]' '[:lower:]')_$id
      cd $(echo "$1" | tr '[:upper:]' '[:lower:]')_$id
      defects4j checkout -p $1 -v ${id}b -w ./
      cd $script_folder
      python defects4j-g5k-node.py -project $1 -tool Genprog -id $id
    done
  elif [ "$1" = "Lang" ]; then
    cd $project_folder
    mkdir $(echo "$1" | tr '[:upper:]' '[:lower:]')
    for id in {1..65}
    do
      cd ${project_folder}/$(echo "$1" | tr '[:upper:]' '[:lower:]')
      mkdir $(echo "$1" | tr '[:upper:]' '[:lower:]')_$id
      cd $(echo "$1" | tr '[:upper:]' '[:lower:]')_$id
      defects4j checkout -p $1 -v ${id}b -w ./
      cd $script_folder
      python defects4j-g5k-node.py -project $1 -tool Genprog -id $id
    done
  elif [ "$1" = "Mockito" ]; then
    cd $project_folder
    mkdir $(echo "$1" | tr '[:upper:]' '[:lower:]')
    for id in {1..38}
    do
      cd ${project_folder}/$(echo "$1" | tr '[:upper:]' '[:lower:]')
      mkdir $(echo "$1" | tr '[:upper:]' '[:lower:]')_$id
      cd $(echo "$1" | tr '[:upper:]' '[:lower:]')_$id
      defects4j checkout -p $1 -v ${id}b -w ./
      cd $script_folder
      python defects4j-g5k-node.py -project $1 -tool Genprog -id $id
    done
  elif [ "$1" = "Time" ]; then
    cd $project_folder
    mkdir $(echo "$1" | tr '[:upper:]' '[:lower:]')
    for id in {1..27}
    do
      cd ${project_folder}/$(echo "$1" | tr '[:upper:]' '[:lower:]')
      mkdir $(echo "$1" | tr '[:upper:]' '[:lower:]')_$id
      cd $(echo "$1" | tr '[:upper:]' '[:lower:]')_$id
      defects4j checkout -p $1 -v ${id}b -w ./
      cd $script_folder
      python defects4j-g5k-node.py -project $1 -tool Genprog -id $id
    done
  fi
else
  python defects4j-g5k-node.py -project $1 -tool Genprog -id $2
fi

#python defects4j-g5k-node.py -project $1 -tool Genprog -id $2
