#!/usr/bin/env bash

# find all .jpg images in current directory (without going into subdirectories)
# and merge them into the output.mp4 file using ffmpeg
# if all is ok then prints command to delete images

files=$(find . -maxdepth 1 -name '*.jpg' -print)

if [ -z "$files" ]; then
  echo "No files found, nothing to do."
  exit 0
fi

cat $(find . -maxdepth 1 -name '*.jpg' -print | sort -V) | ffmpeg -y -framerate 15 -i - -c:v libx264 -crf 25 -vf format=yuv420p -movflags +faststart output.mp4
result=$?

if [ $result -eq 0 ]; then
   echo "Deleting source files"
   echo find . -maxdepth 1 -name '*.jpg' -delete
fi
