# Configuring esp32


## First install

- prepare esp32 device and USB cable
- initiate esp32 installation using [esphome web](https://web.esphome.io/)
- connect your device to the usb cable and into the computer
- press `Connect` in esphome web, wait until it configures the device

## Run esphome dashboard

- the easiest is to run container with esphome and use it for device config
- new device should show up - press adopt and configure it (see below)
- TODO: add comments to esphome dasboard?
- TODO: how to add secrets to wifi

## Install firmware on the device

- press `Edit` on the device
- copy paste code from `../esphome/esp32-camera.yaml`
- edit entries such as passwords, device name, make sure to alter entries
  related to your camera (depending on camera you need to change it)
- check code (we ui should automatically do this)
- install code over web
- go to esp32 address (`ESP32_CAMERA_ADDRESS`),
  check if web address returns screenshot on port `8081`
