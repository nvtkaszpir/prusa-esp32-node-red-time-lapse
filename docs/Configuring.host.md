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

- install node-RED
  see [docs](https://nodered.org/docs/getting-started/local)

- configure node-RED by installing extra plugins
  required plugins
  - `node-red-contrib-file-manager` - write files
  - `node-red-contrib-image-output` - image preview
  - `node-red-contrib-moment` - timestamp formatting
  - `node-red-contrib-ui-led` - web ui component
  - `node-red-dashboard` - web UI

- accessing node-RED dashboard
  - go to address of the node-red and append `/ui` at the end of the address

## In docker containers

```shell
cd docker
docker-compose up -d
```
