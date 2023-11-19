# Fake Prusa Mini+ API

Simulates very basic Prusa Mini+ API ( to be precise [openapi-legacy](https://github.com/prusa3d/Prusa-Link-Web/blob/master/spec/openapi-legacy.yaml),
by running flask with static content and toggle button to switch between 'printing' and 'not printing' state, so
it is easier to test code with other tools.

## Usage

Locally with [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv):

```bash
pyenv virtualenv fake-prusa
pyenv activate fake-prusa
pip install -r requirements.txt

flask run --debug --host 0.0.0.0 --port 5000
```

Or using docker containers:

```bash
docker build -t fake-prusa:dev .
docker run -it -p 5000:5000 fake-prusa:dev
```
