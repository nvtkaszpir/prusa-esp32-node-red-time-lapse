# Configuring custom gcode

## Overview

Triggering photo per layer gives much better time lapse images and thus much better
time lapse videos in general - no more moving elements, so no more print object
obstructed by printing head etc, also photographed object is always in predefined location.
In general it makes process a bit more complex but tremendously improves quality of the
video outputs.

To trigger physical button it is required to use custom gcodes in the
model slicing software, such as PrusaSlicer.

Current code is for PrusaMini+ and it moves print head to the middle back of the print
bed and then towards Z axis (to trigger press button) and then moves back again
to the middle back of the print bed and continues normal print for the next layer.

I've added retraction to avoid oozing, but that may not be needed if filament is properly
dried.

Notice that you may need to just extract fragments of the gcode if you need to adjust
it to different printer, see the comments in the code where the given section starts
or ends.

In my esp32 I need to wait around 3500ms to capture really clean photo,
because 2500ms were just a bit too low in extremely rare cases (1/100).

If you print is big enough then those delays are negligible.

## How to apply changes

In PrusaSlicer update `Printer Settings` corresponding sections with the contents
of the files from [gcode/](gcode/) directory.

Save settings as new printer profile and use it for slicing from now on.

Then ensure to slice model and use it in the print.
You can use PrusaSlicer preview and bottom progress bar to see how the print head will move,
which is very useful to see if the print head actually trigger the physical button.
