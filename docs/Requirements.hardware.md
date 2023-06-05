# Hardware requirements

- 3D printer connected via Ethernet to the LAN - Prusa Mini+ has this and is
  exposing its API, we need only reading capability. I believe the code could
  be adjusted to any printer which exposes web interface.

- camera - esp32 (in my case esp32-wrover-e) with camera OV2640, or you could
  just get esp32-cam which is all-in-one integrated solution - make sure to
  get an USB bridge, though, it makes firmware updates way easier.
  Frankly speaking if you have any camera that allows to fetch still image
  via web then it would work.

- camera mount - to get best time-lapse images camera should be attached
  firmly to print bed. This
  [model](https://www.printables.com/model/18795-prusa-i3-mk3-camera-holder) 
  for Prusa MK3fits into the mounting for Prusa Mini.
  Notice to install it in such way so that it does not touch hotbed.
  Using something like felt can limit amount of heat going through. 
  Adding little ridges (to prevent zip tie to move) and zip tie will make it
  good enough to be stable.

- USB-A to micro-USB cable - to power esp32 and camera.

- host - additional hardware - any computer, which used to host some
  extra apps mentioned below. I recommend any Raspberry Pi, with a note that 
  Raspberry Pi Zero W also should be capable but merging images to
  videos will be noticeably slower.

- network - WiFi bridged with LAN, for wireless connection between host,
  esp32 and the 3D printer.

- 5V power adapter - optional, to power esp32, could use USB-A hub splitter 
  and connect it to printer port.

- LED lights - optional, to mount above printed to make better conditions
  for taking pictures
