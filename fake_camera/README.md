# Fake Camera

Simulates very basic esp32 camera output.
Make sure to run it on different port than fake-prusa-api.

## Usage

```bash
pyenv virtualenv fake-camera
pyenv activate fake-camera
pip install -r requirements.txt
flask run --debug --host 0.0.0.0 --port 8888
```

```bash
docker build -t fake-esp32camera:dev .
docker run -it -p 8888:8888 fake-esp32camera:dev
```
