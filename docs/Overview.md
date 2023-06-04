# Overview

**NOTICE**:

- this is a proof of concept setup, not seruity measures were taken to restrict
  access to the system. Use at your own risk

Initial idea:

- making time lapse videos without any special software which would control
  3D printer - PrusaSlicer and original Prusa firmware are just working
  perfectly well in my case, so I wanted to avoid any software that alters
  `gcode` or requires access printer via USB.
  The fact that Prusa Mini has basic web API makes this possible. 
- taking photos would depend on if the printer is up and printing, there is
  no point in capturing images if printer is off or not printing, at least
  just for time-lapse videos.
- taking photos does not have to be realitme or fast, we usually need
  image once per 10 seconds.
- I know I can add printer to HomeAssistant, but my experience with
  HomeAssistant is a bit problematic, mainly because development phase.
  I've decided to try something I always wanted to use but never had
  an urge to implement, and that is [node-RED](https://nodered.org/) .
