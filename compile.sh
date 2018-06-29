#!/bin/bash

if javac -cp /Users/zimin/Desktop/KTH/Master-Thesis/defects4j-repair-runner/commons-cli-1.4.jar:/Users/zimin/Desktop/KTH/Master-Thesis/defects4j-repair-runner/astor-0.0.2-SNAPSHOT-jar-with-dependencies.jar:/Users/zimin/Desktop/KTH/Master-Thesis/defects4j-repair-runner/ main.java;
then
  echo 'Compilation done!'
else
  echo 'Compilation failed'
fi
