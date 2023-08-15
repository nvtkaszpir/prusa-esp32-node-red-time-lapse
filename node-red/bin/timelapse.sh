#!/usr/bin/env bash

# find all .jpg images in current directory (without going into subdirectories)
# and merge them into the output.mp4 file using ffmpeg
# if all is ok then prints command to delete images

# pass directory name as param
if [ -n "$1" ]; then
    echo "Entering $1"
    pushd "$1"
fi

echo "Finding images..."
files=$(find . -maxdepth 1 -name '*.jpg' -print)

if [ -z "$files" ]; then
  echo "No files found, nothing to do."
  exit 0
fi

output_file=$( basename $PWD )
echo "Generating output to ${output_file}.mp4"
# list by time ascending
cat $(ls -1tr *.jpg) | ffmpeg -y -framerate 15 -i - -c:v libx264 -crf 25 -vf format=yuv420p -movflags +faststart ${output_file}.mp4
result=$?
echo "result=$result"

if [ $result -eq 0 ]; then
   echo "To delete source files, please run below commands:"
   echo $PWD
   echo find . -maxdepth 1 -name '*.jpg' -delete
fi

