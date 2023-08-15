# prusa-esp32-node-red-time-lapse

Taking time lapse videos from Prusa prints using esp32 camera and Node-RED.

Node-RED checks periodically if printer is up and printing.
If it prints then Node-RED takes picture via web from esp32 camera,
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
- [Hacking](docs/Hacking.md)


https://github.com/nvtkaszpir/prusa-esp32-node-red-time-lapse/assets/1480252/9d08c0c2-bd34-430f-b20b-ba48656a8d91


![printer status flow](docs/static/prusa_printer_status-fs8.png)

![web_ui](docs/static/web_ui-fs8.png)


## What works

- Node-RED + mqtt in containers (docker), can also run directly on host
- logic flow - capturing images to directory if printer is printing
- rendering images into a movie using ffmpeg within node-red container
- now whole process is within single flow, and you can run multiple flows if you have different printers/cameras
- you can define default values per flow such as destination directory, printer address, camera address
- if day change is detected (via UTC) then print counter is reset to zero after current print is finished
- fetch image from camera only once
- ffmpeg in container + shell script to merge images into a mp4 file
- basic web ui dashboard, it's crap but provides core info :)

- default docker-compose spawns fake prusa api and fake esp32 camera,
  this is great to test flows and adjust them without need of using real hardware
- fixed issues with out of order frames

## Known limitations

- you MUST configure node `general config` under `on Startup` and set vars there

![config](docs/static/config-fs8.png)

- screenshot taking/stopping and video render have some delay, this is intentional,
  first, it allows to add 'final' frame when printer head is away from print,
  second, it allows to not trigger actions on failed messages
- before rendering videos there is not much info on the dashboard
- video progress is showing yellow dot only if ffmpeg runs for over 10s
- can not get rendered video from the dashboard - out of scope -use other flows for that,
  there is one that allows to browse files via web ui ,
  or just mount data dir as samba share etc
- if camera fetch error occurs there is no retry to fetch it,
  this is rather not an issue because ffmpeg will automatically detect incorrect images
  and will not add them to video
- rendered images and videos are not cleaned up, you must manage data dir on your own


## TODO

- ? script to process dumped flow and strip sensitive data with jq, so that
  it can be added to git safely

- ? script to process flows from git with secrets.json to replace entries,
  also provide secrets.json.dist as an example for input with some comments

## NOT-TODO

Things that will not going to happen:

- adding code to list files for render videos/images in web ui;
  there are other better solutions there such as
  [Csongor Varga code](https://flows.nodered.org/flow/44bc7ad491aacb4253dd8a5f757b5407)
