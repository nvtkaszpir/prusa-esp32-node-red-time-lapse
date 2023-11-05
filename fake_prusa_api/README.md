# Fake Prusa Mini+ API

Simulates very basic Prusa Mini+ API, by running flask with static content and
toggle button to switch between 'printing' and 'not printing' state, so
it is easier to test code with other tools.

## Usage

```bash
pyenv virtualenv fake-prusa
pyenv activate fake-prusa
pip install -r requirements.txt

flask run --debug --host 0.0.0.0 --port 5000
```

```bash
docker build -t fake-prusa:dev .
docker run -it -p 5000:5000 fake-prusa:dev
```
