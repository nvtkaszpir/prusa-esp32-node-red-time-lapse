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
  firmly to some static base on which printer is placed (can be enclosure).
  Notice to install it in such way so that it does not touch hotbed.
  The best is to place it in such spot that it will capture whole print
  bed with the full model height.

- physical button - get any physical button to be used with electronics,
  this can be [reed switch](https://en.wikipedia.org/wiki/Reed_switch) which
  is triggered byt the little magnet getting close to it, or
  [limit microswitch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch)

- (optional) magnet to trigger button - can be something like 8x3mm neodymium magnet
  if using reed switch

- USB-A to micro-USB cable - to power esp32 and camera and initial flashing

- host - additional hardware - any computer, which used to host some
  extra apps mentioned below. I recommend any Raspberry Pi, with a note that
  Raspberry Pi Zero W also should be capable but merging images to
  videos will be noticeably slower.

- network - WiFi bridged with LAN, for wireless connection between host,
  esp32 and the 3D printer.

- 5V power adapter - optional, to power esp32, could use USB-A hub splitter
  and connect it to printer port, but it is better to power esp32 idependently

- (optional) single color LED + 220 Ohm resistors + cables - if you want extra signals
  to see that printing is in action and camera capture was triggered

- cables to attach physical button to the esp32 pins,
  for example jumper/Dupont wires, for the button I recomment at least 50cm
  and for the LEDs something about 5cm

- (optional) LED lights - to mount above printed to make better conditions
  for taking pictures
