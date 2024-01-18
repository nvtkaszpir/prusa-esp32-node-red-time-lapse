# Custom gcode

A set of custom gcodes to add to PrusaSlicer to allow triggering physical button
press per layer change.

See [Configuring custom gcode](docs/Configuring.gcodem.md).

Some comments:

- do not add any custom Z moves in custom gcode, you probbaly want to adjust
  Printer > Extruder > Travel Lift > Lift Height

- `G1 X{round(print_bed_size[0]/2)} Y{print_bed_size[1]} F{travel_speed*60} ; move head back in the middle`
  means move (G1) to X`bed_size_x/2` Y`bed_size_y` so it is auto calculated to your current bed size
  which means it works on any printer :)
  so for Prusa Mini which as max x 180 and max y 180 then the code becomes
  `G1 X90 Y180`
- default custom gcode assumes you have a physical button on the Z axis, which
  is triggered if you move print head to `X180 Y180` on Prusa Mini+, but
  if you want to move the button to the opposite side of the axis then change
  code to something like below:

  ```text

  ; take a photo start
  G1 X{round(print_bed_size[0]/2)} Y{print_bed_size[1]} F{travel_speed*60} ; move head back in the middle
  G4 S0 ; Wait for move to finish

  G1 X0 Y{print_bed_size[1]} F{travel_speed*60} ; trigger button activation
  G4 S0 ; Wait for move to finish
  G4 P3500 ; Wait for image capture in miliseconds

  G1 X{round(print_bed_size[0]/2)} Y{print_bed_size[1]} F{travel_speed*60} ; move head back in the middle
  G4 S0 ; Wait for move to finish
  ; take a photo end
  G1 E1 F2100 ; revert rectraction after photo
  ```
