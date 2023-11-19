# Overview

**NOTICE**:

This is a proof of concept setup, no security measures were taken to restrict
access to the system. Use at your own risk

Initial idea:

- making time lapse videos without any special software which would control
  3D printer - PrusaSlicer and original Prusa firmware are just working
  perfectly well in my case, so I wanted to avoid any specialized software
  that alters `gcode` in realtime or requires access printer via USB.
  The fact that Prusa Mini has basic web API and PrusaSlicer allows defining
  custom gcode per layer makes this possible.

- above assumes that custom gcode per layer is used trigger physical button
  to further trigger image capture

- taking photos would depend on if the printer is up and printing, there is
  no point in capturing images if printer is off or not printing, at least
  just for time-lapse videos.

- taking photos does not have to be real time or fast, we usually need
  image once per layer captured in some sane time (such as under 2s)

- I know I can add printer to HomeAssistant, but my experience with
  HomeAssistant is a bit problematic, mainly because development phase.
  I've decided to try something I always wanted to use but never had
  an urge to implement, and that is [Node-RED](https://nodered.org/) .
