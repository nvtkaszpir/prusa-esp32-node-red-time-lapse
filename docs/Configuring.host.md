# Configuring host

## Directly on host

- check connectivity from host to printer and esp32 via curl or wget
- install ffmpeg
  ```shell
  apt-get update
  apt-get install -y ffmpeg
  ```

- install MQTT server
  ```shell
  apt-get update
  apt-get install -y mosquitto
  ```

- configure MQTT server
  see example `mqtt/config/` dir

- install Node-RED
  see [docs](https://nodered.org/docs/getting-started/local)

- configure Node-RED by installing extra plugins
  required plugins - this can be done via `Manage Palette`
  or `npm install <package-name>`, Dockerfile already has it:
    ```shell
    node-red-contrib-counter
    node-red-contrib-image-output
    node-red-contrib-moment
    node-red-contrib-simple-gate
    node-red-contrib-ui-led
    node-red-dashboard
    ```


## In docker containers

```shell
cd docker
docker-compose up -d --build
```

### docker-compose service endpoints

- accessing Node-RED editor - http://127.0.0.1:1880
- accessing Node-RED dashboard - http://127.0.0.1:1880/ui
- accessing fake prusa API - http://127.0.0.1:5000/
- accessing fake esp32 camera - http://127.0.0.1:8888/
