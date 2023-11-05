# Prusa Mini API examples

Prusa Mini+ 4.4.1

## printing preheat

printer:

```text
{"telemetry":{
  "temp-bed":36.3,"temp-nozzle":92.9,"print-speed":100,"z-height":0.0,"material":"PETG"
  },
"temperature":{
  "tool0":{"actual":92.9,"target":170.0,"display":170.0,"offset":0},
  "bed":{"actual":36.3,"target":85.0,"offset":0}},
"state":{
  "text":"Printing",
  "flags":{
    "operational":false,"paused":false,"printing":true,"cancelling":false,"pausing":false,"sdReady":false,"error":false,"closedOnError":false,"ready":false,"busy":false}}}
```

job:

```text
{"state":"Printing",
  "job":{
    "estimatedPrintTime":699,
    "file":{
      "name":"ESP32Cam-Clamp_0.2mm_PETG_MINI_12m.gcode",
      "path":"/usb/ESP32C~1.GCO",
      "display":"ESP32Cam-Clamp_0.2mm_PETG_MINI_12m.gcode"
    }
  },
  "progress":{
    "completion":0.00,"printTime":39,"printTimeLeft":660}}
```

## print finished, waiting in menu on 100%

printer:

```text
{"telemetry":{"temp-bed":27.3,"temp-nozzle":26.9,"print-speed":100,"z-height":39.1,"material":"PETG"},
"temperature":{
  "tool0":{"actual":26.9,"target":0.0,"display":0.0,"offset":0},
  "bed":{"actual":27.3,"target":0.0,"offset":0}},
"state":{
  "text":"Operational",
  "flags":{
    "operational":true,"paused":false,"printing":false,"cancelling":false,"pausing":false,"sdReady":false,"error":false,"closedOnError":false,"ready":true,"busy":false}}}
```

job:

```text
{"state":"Operational","job": null,"progress": null}
```

## normal idle in menu

printer:

```text
{"telemetry":{"temp-bed":27.3,"temp-nozzle":26.8,"print-speed":100,"z-height":39.1,"material":"PETG"},
"temperature":{
    "tool0":{"actual":26.8,"target":0.0,"display":0.0,"offset":0},
    "bed":{"actual":27.3,"target":0.0,"offset":0}},
"state":{
    "text":"Operational",
    "flags":{
        "operational":true,"paused":false,"printing":false,"cancelling":false,"pausing":false,"sdReady":false,"error":false,"closedOnError":false,"ready":true,"busy":false}}}
```

job:

```text
{"state":"Operational","job": null,"progress": null}
```
