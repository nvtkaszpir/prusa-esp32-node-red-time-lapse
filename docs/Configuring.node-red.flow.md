# Configuring Node-RED flow

All is merged into a single flow.
If needed you can copy flow if you need multiple printers etc.

## Details

- make sure to have installed extra nodes
  (see [Configuring Host](Configuring.host.md))

- make sure esp32 camera and 3D printer works

### Detailed howto

- go to Node-RED editor [http://127.0.0.1:1880/](http://127.0.0.1:1880/)
- import `flows/prusa_v1.json` to Node-RED.
- if you have duplicated elements then replace them (especially for web-ui)
- edit node `general config` in top left corner, in the tab `On Start`,
  edit `save_path_root` if you have different printers to avoid file save overwrites and overall mess
  for example `/data/prusa/my-printer-1`;
  set printer endpoint and access key (`printer_api_address` and `printer_api_key`);
  set esp32 camera address endpoint (`esp32_camera_address`);
  double check ports used!
  TODO: configure mqtt topic
- deploy flows
- check Node-RED web ui for status [http://127.0.0.1:1880/ui](http://127.0.0.1:1880/ui)
- check if pressing button triggers sending message to MQTT
- check if the flow in Node-RED is triggered from mqtt message topic - that's why leds are useful
  because you should get back led light if flow was triggered
- try example print - see [Capturing video](Capturing.video.md)
