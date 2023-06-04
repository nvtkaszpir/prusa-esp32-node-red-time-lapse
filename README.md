# prusa-esp32-node-red-time-lapse
Taking time lapse videos from Prusa prints using esp32 camera and node-red

## Overview

Initial idea:

- making time lapse videos without any special software which would control
  3D printer, that is I wanted to avoid any software that alters `gcode`
  or requires access printer via USB. The fact that Prusa Mini has basic web API makes this possible.
- taking photos would depend on if the printer is up and printing, there is
  no point in capturing images if printer is off or not printing, at least
  just for time-lapse videos.
- taking photos does not have to be realitme or fast, we usually need
  image once per 10 seconds.
- I know I can add printer to HomeAssistant, but my experience with
  HomeAssistant is a bit problematic, mainly because development phase.
  I've decided to try something I always wanted to use but never had
  an urge to implement, and that is [node-RED](https://nodered.org/) .

## Hardware requirements

- printer - Prusa Mini+ connected via ethernet to the LAN, exposing its API, 
  we need only reading capability. I believe the code could be adjusted to
  any printer which exposes web interface.

- camera - esp32 (in my case esp32-wrover-e) with camera OV2640, or you could
  just get esp32-cam which is all-in-one integrated solution (make sure to
  get an SUB bridge, though, it makes firmware updates way easier.
  Frankly speaking if you have any camera that allows to fetch still image
  via web then it would work.

- host - additional hardware - any computer, which used to host some
  extra apps mentioned below. I recommend any Raspberry Pi, with a note that 
  Raspberry Pi Zero W also should be capable but merging images to
  videos will be noticeably slower.

## Software requirements

- esp32 - any code that can grab camera still image via web, the easiest
  for now is to install [esphome](https://esphome.io/) with [camera](https://esphome.io/components/esp32_camera.html) with [web component](https://esphome.io/components/esp32_camera_web_server.html)
- MQTT server (via mosquitto) which is required for node-RED to operate
  can be installed in container or directly on host
- logic - [node-RED](https://nodered.org/) with the flows which holds and 
  executes the logic if the photo should be taken and stored. Can be installed
  in container or directly on host
- extra app to process images into a movie - [ffmpeg](https://ffmpeg.org/)
  will work here very well

## What works

- node-RED + mqtt in containers (docker), could be run directly on host
- logic flow - capturing images to directory if printer is printing
- rendering images into a movie using ffmpeg (externally executed)

## Known limitations

- only one printer/one camera is supported - would require better modularization

- all images are dumped into one directory, I'm planning to add variable to detect if the print is happening and when it started to create directory and store images there - easier to manage if printing more than one thing in a sequence

- due to the fact I run it in container which does not have ffmpeg I need to manually execute script to merge images into a video, I bet that can be fixed by just installing ffmpeg within container but for now I wanted to avoid it.
Will do updates later on

- basic web ui dashboard, it's crap but provides core info :)

