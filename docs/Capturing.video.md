# Capturing images

## Using default docker-compose

- on default setup you will get docker-compose and spawned containers
  which can be used to fake real hardware

- `fake-prusa` fakes Prusa Mini+ API, see port `5000` for more,
  you can press on/off button to simulate printer operation,
  remember there is a delay before print so be patient (like 30s)

- `fake-esp32camera` fakes esp32 camera, and on port `8888` it just returns
  some black text on gray background

## Using real hardware

- if above works, just update `generic config` in the flow
  and provide real endpoints data for printer and the camera
  and press deploy

- if this is correct you should see real camera image preview

- for more details see Node-RED dashboard ui

- if all works just start printing something small in 3D printer,
  for example [calibration cube](https://www.printables.com/search/models?q=calibration%20cube),
  as a result if you have red led attached it should start to glow red,
  and green led should flash with every layer printed

- Check destination directory where Node-RED writes files, there
  should be a new JPG file every printed layer

- when stopping short print then after about 40s check if there is an
  output of the rendered video;
  of course longer prints and higher resolution images will get noticeably more time to process

- all in all after any print (successful or failed) you should get a .mp4 file,
  which should correspond to the images captured with every layer printed.
