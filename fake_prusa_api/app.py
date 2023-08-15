from flask import Flask
from flask import json
from flask import render_template
from flask import request

app = Flask(__name__)

printer = {
    "status": "Operational",
    "flags": {
        "operational": True,
        "paused": False,
        "printing": False,
        "cancelling": False,
        "pausing": False,
        "sdReady": False,
        "error": False,
        "closedOnError": False,
        "ready": True,
        "busy": False,
    },
}

job = {
    "state": "Operational",
    "job": None,
    "progress": None,
}


@app.route("/health")
def health():
    result ="OK"
    return result

@app.route("/")
def index():
    return render_template("app.html")


@app.route("/api/printer")
def printer_status():
    msg = {
        "telemetry": {
            "temp-bed": 36.3,
            "temp-nozzle": 92.9,
            "print-speed": 100,
            "z-height": 0.0,
            "material": "PETG",
        },
        "temperature": {
            "tool0": {"actual": 92.9, "target": 170.0, "display": 170.0, "offset": 0},
            "bed": {
                "actual": 36.3,
                "target": 85.0,
                "offset": 0,
            },
        },
        "state": {
            "text": printer["status"],
            "flags": printer["flags"],
        },
    }

    response = app.response_class(
        response=json.dumps(msg), status=200, mimetype="application/json"
    )
    return response


@app.route("/api/job")
def job_status():
    msg = {
        "state": job["state"],
        "job": job["job"],
        "progress": job["progress"],
    }

    response = app.response_class(
        response=json.dumps(msg), status=200, mimetype="application/json"
    )
    return response


@app.route("/get_toggled_status")
def toggled_status():
    current_status = request.args.get("status")
    if current_status == "Not Printing":
        printer["status"] = "Printing"
        printer["flags"] = {
            "operational": False,
            "paused": False,
            "printing": True,
            "cancelling": False,
            "pausing": False,
            "sdReady": False,
            "error": False,
            "closedOnError": False,
            "ready": False,
            "busy": False,
        }

        job["state"] = "Printing"
        job["job"] = {
            "estimatedPrintTime": 699,
            "file": {
                "name": "ESP32Cam-Clamp_0.2mm_PETG_MINI_12m.gcode",
                "path": "/usb/ESP32C~1.GCO",
                "display": "ESP32Cam-Clamp_0.2mm_PETG_MINI_12m.gcode",
            },
        }
        job["progress"] = {
            "completion": 0.00,
            "printTime": 39,
            "printTimeLeft": 660,
        }
        return "Printing"
    else:
        printer["status"] = "Operational"
        printer["flags"] = {
            "operational": True,
            "paused": False,
            "printing": False,
            "cancelling": False,
            "pausing": False,
            "sdReady": False,
            "error": False,
            "closedOnError": False,
            "ready": True,
            "busy": False,
        }

        job["state"] = "Operational"
        job["job"] = None
        job["progress"] = None

        return "Not Printing"


if __name__ == "__main__":
    app.run()
