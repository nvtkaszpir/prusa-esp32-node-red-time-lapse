# Configuring node-RED flow

Notice that current code consists of two flows.
One is just to test printer status, if specific criteria is met it triggers
another flow.
Second flow is just to capture and store image in directory.

## Details

- make sure to have installed extra nodes
  (see [Configuring Host](Configuring.host.md))
- import flow into the node-red
- edit specific flow nodes
  - `Prusa Printer Status` - replace `PRUSA_MINI_HOST_ADDRESS` and in Headers
    replace `PRUSA_API_KEY`
  - `Capture ESP32 Camera Screenshot` - replace `ESP32_CAMERA_ADDRESS`
  - in `template` change `/data/prusa/{{payload}}.jpg` to location where you
   want to store file (assuming /data is mounted under node-red container)
- deploy node red flows
- test if capturing image works - you can manually trigger flow in node-red
- test if printer status is up
- testing print and automation - when 3D printing then new images should show
  up in target directory
