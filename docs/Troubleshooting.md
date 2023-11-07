# Troubleshooting

Check each component separately, such as:

- if devices are on the same network
- if printer API works (api key?)
- if endpoints are available, such as node-red->printer, node-red->camera
- if device camera works
- if button works (should be in esphome web logs for device)
- esp32 device -> mqtt broker
- node-red -> mqtt broker
- writing to the node-red data directory
- computing power requirements (for example if ffmpeg + pi zero actually would not melt ;D )
- if the printer actually prints + node-red flows logic
- node-red endpoints + api keys + delays
