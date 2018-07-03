#!/bin/bash

if javac -cp /mnt/vdb1/home/ubuntu/defects4j-repair-runner/commons-cli-1.4.jar:/mnt/vdb1/home/ubuntu/defects4j-repair-runner/astor-0.0.2-SNAPSHOT-jar-with-dependencies.jar:/mnt/vdb1/home/ubuntu/defects4j-repair-runner/ main.java;
then
  echo 'Compilation done!'
else
  echo 'Compilation failed'
fi
