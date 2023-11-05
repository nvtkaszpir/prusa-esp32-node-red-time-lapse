# Preparing hardware

Connecting cables to the devices may require soldering,
especially to button and LED legs.

## Button

- attach jumper wires to the physical button,
  watch out which connectors you use, because some have common mass

- attach physical button to the `GPIO13` and any `GND` pin on esp32

- attach button to the printer body so that print movement will trigger
  its action.

- if using reed switch then attach magnet to the print head, can be a metal
  or plastic strip screwed to the print head, and magnet on the end of the strip.

  TODO: add photo

- if using limit microswitch it may require printing switch mounting
  TODO: add url to my dumb model, upload model to repo

## Signaling LEDs

- attach resistors to color LEDs and attach jumper wires
- connect LED cables to the esp32, make sure you do not mix polarity
  TODO: add more details about polarity and pins
