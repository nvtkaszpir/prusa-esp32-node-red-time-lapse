# Software requirements

- esp32 - any code that can grab camera still image via web, the easiest
  for now is to install [esphome](https://esphome.io/) with
  [camera](https://esphome.io/components/esp32_camera.html) with
  [web component](https://esphome.io/components/esp32_camera_web_server.html)

- middleware - MQTT server (via mosquitto) which is required for Node-RED to operate
  can be installed in container or directly on the host

- logic - [Node-RED](https://nodered.org/) with the flows which holds and
  executes the logic if the photo should be taken and stored. Can be installed
  in container or directly on host

- (optional) extra app to process images into a movie - [ffmpeg](https://ffmpeg.org/)
  will work here very well, this is already integrated in Node-RED used
  by docker-compose in this repo

- 3D printer network enabled and access key - when you configure printer
  via LCD menu, then there is an option to show access key for the API.
  Write that down. More info in [printer details](Printer.details.md)

- software to generate gcode from sliced model to be used for print,
  in here it will be [PrusaSlicer](https://github.com/prusa3d/PrusaSlicer/releases).
