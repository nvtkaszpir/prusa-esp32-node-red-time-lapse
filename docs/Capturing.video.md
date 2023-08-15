# Capturing images

# Using default docker-compose

- on default setup you will get docker-compose and spawned containers
  which can be used to fake real hardware
- fake_prusa fakes Prusa Mini+ API, see port 5000 for more,
  you can press on/off button to simulate printer operation,
  remember there is a delay before print so be patient (like 30s)
- fake_camera fakes esp32 camera, and on port 8888 it just returns
  some black text on gray background

# Using real hardware

- if above works, just update `generic config` in the flow
  and provide real endpoints data for printer and the camera
  and press deploy
- if this is correct you should see real camera image preview
- for the printer see dashboard ui
- If all works just start printing something in 3D printer,
  you can actually try to print something for 1 minute and abort
  and this should still work!
- Check destination directory where Node-RED writes files, there
  should be a new file every 10 seconds.
- after about 40s check if there is an output of the rendered video

