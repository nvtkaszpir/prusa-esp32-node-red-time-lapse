"""
render fake screesnhot
make sure to host it on different port than fake printer api
"""
from datetime import datetime
from flask import Flask
from flask import send_file
from io import BytesIO
from PIL import Image, ImageFont, ImageDraw
import os

port = 8888 # yeah whatever
host = os.getenv("HOSTNAME")
width = 640
height = 480

camera = Flask(__name__)

@camera.route("/health")
def health():
    result ="OK"
    return result

@camera.route("/")
def index():
    # prepare image and write timestamp on it
    img  = Image.new(mode="RGB", size=(width, height), color=(200,200,200))
    img_draw = ImageDraw.Draw(img)
    time_now = datetime.utcnow()
    text = "fake_esp32camera \n"
    text += f"hostname: {host} \n"
    text += f"port: {port} \n"
    text += "\n"
    text += time_now.strftime("%Y-%m-%d %H:%M:%S") + " UTC"
    text += "\n\nThis is dummy image to \nfake camera image capture"
    font = ImageFont.truetype("DejaVuSans.ttf", size=30)
    img_draw.text((20, 20), text=text, font=font, fill=(0, 0, 0))
    stream = BytesIO()
    img.save(stream, "JPEG", quality=80, optimize=True, progressive=True)
    stream.seek(0)
    result = send_file(stream, mimetype='image/jpeg')
    return result

if __name__ == "__main__":
    camera.run()
