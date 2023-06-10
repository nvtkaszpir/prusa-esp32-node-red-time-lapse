# prusa-esp32-node-red-time-lapse

Taking time lapse videos from Prusa prints using esp32 camera and Node-RED.

Node-RED checks periodically if printer is up and printing.
If it prints then Node-RED takes picutre via web from esp32 camera,
and stores it in local directory.
After print images can be merged into a .mp4 movie.

Details:

- [Overview](docs/Overview.md)
- [Hardware Requirements](docs/Requirements.hardware.md)
- [Software Requirements](docs/Requirements.software.md)
- [Configuring esp32](docs/Configuring.esp32.md)
- [Configuring printer](docs/Configuring.printer.md)
- [Configuring host](docs/Configuring.host.md)
- [Node-RED Flow configuration](docs/Configuring.node-red.flow.md)
- [Capturing images and making video](docs/Capturing.video.md)
- [Further steps](docs/Further.steps.md)


https://github.com/nvtkaszpir/prusa-esp32-node-red-time-lapse/assets/1480252/9d08c0c2-bd34-430f-b20b-ba48656a8d91


## What works

- Node-RED + mqtt in containers (docker), could be run directly on host
- logic flow - capturing images to directory if printer is printing
- rendering images into a movie using ffmpeg (externally executed)

## Known limitations

- could be as one flow, right now camera image is fetched twice
- only one printer/one camera is supported - would require better modularization

- all images are dumped into one directory, I'm planning to add variable to
  detect if the print is happening and when it started to create directory
  and store images there - easier to manage if printing more than one thing in
  a sequence

- ffmpeg in container but no automation to merge images in flows

- basic web ui dashboard, it's crap but provides core info :)

![printer status flow](docs/static/prusa_printer_status-fs8.png)

![cam screenshot flow](docs/static/prusa_cam_screenshot-fs8.png)


![web_ui](docs/static/web_ui-fs8.png)

## TODO

- script to process dumped flow and strip sensitive data with jq, so that
  it can be added to git safely

- script to process flows from git with secrets.json to replace entries,
  also provide secrets.json.dist as an example for input with some comments

- check docker-compose

- make Dockerfile for Node-RED with ffmpeg

- merge flows into one with optional trigger?

- do single trigger and fetch image from esp32 once
  and based on printer status save it

- take printer model or some unique printing id + print start time
  and set it as target directory name and save files there

- if printer was printing for lest say 1min and stops printing
  then trigger script to merge images to video,
  detect printer state if paused or waiting for action

- we got mp4, now what? Node-RED web expose?
  what about file cleanups after some time?