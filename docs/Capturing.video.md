# Capturing images

- If all works just start printing something in 3D printer.
- Chekc destination directory where Node-RED writes files, there
  should be a new file every 10 seconds.

# Making video

- The best way is to move files to subdirectory
- in subdirectory run `bin/prusa_timelapse.sh` - it should merge all
  .jpg images into output.mp4 file
- any soft errors should be handled by ffmpeg, such as corrupt
  jpeg images (sometimes downloading image from esp32 fails)

- tune in shell script if you want more frames per seconds and so on

- remove files if not needed, whatever.

