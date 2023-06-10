# Configuring Node-RED flow

Notice that current code consists of two flows.
One is just to test printer status, if specific criteria is met it triggers
another flow.
Second flow is just to capture and store image in directory.

## Details

- make sure to have installed extra nodes
  (see [Configuring Host](Configuring.host.md))

- make sure esp32 camera and 3D printer works

### Quick Linux howto

- if you have Linux shell then copy `env.dist` to `.env` and replace values,
  then in shell run

  ```shell
  source .env
  envsubst <node-red/capture_esp32_camera_screenshot.json > capture.json
  envsubst <node-red/prusa_printer_status.json > printer_stauts.json
  ```

- go to Node-RED editor http://127.0.0.1:1880/
- import `printer_stauts.json` and `capture.json` to Node-RED.
- if you have duplicated elements then replace them (especially for web-ui)
- deploy flows
- check Node-RED web ui for status http://127.0.0.1:1880/ui

### More detailed howto

Basic procedure below:

- import flows from `node-red/` (`*.json` files) into the Node-RED
- if you have duplicated elements then replace them (especially for web-ui)
- deploy flows
- edit specific flow nodes
  - `Prusa Printer Status` - replace `${PRUSA_MINI_HOST_ADDRESS}` and in Headers
    replace `${PRUSA_API_KEY}`
  - `Capture ESP32 Camera Screenshot` - replace `${ESP32_CAMERA_ADDRESS}`
  - in `template` change `${DEST_PATH}` to location where you
   want to store file (assuming `/data` is mounted under Node-RED container)
- deploy node red flows

- test if capturing image works - you can manually trigger flow in Node-RED
- test if printer status is up
- testing print and automation - when 3D printing then new images should show
  up in target directory
