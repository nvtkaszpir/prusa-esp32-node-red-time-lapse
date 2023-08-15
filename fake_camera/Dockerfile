FROM python:3.10
LABEL org.opencontainers.image.base.name="docker.io/library/python:3.10"
LABEL org.opencontainers.image.authors="kaszpir@gmail.com"
LABEL org.opencontainers.image.description="Basic python app with flask to simulate esp32-camera by outputing jpeg image"
LABEL org.opencontainers.image.url="https://github.com/nvtkaszpir/prusa-esp32-node-red-time-lapse"
LABEL org.opencontainers.image.source="https://github.com/nvtkaszpir/prusa-esp32-node-red-time-lapse"

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
USER nobody

CMD [ "flask", "run", "--host", "0.0.0.0", "--port", "8888", "--debug" ]

EXPOSE 8888/tcp
HEALTHCHECK CMD curl -f http://localhost:8888/health || exit 1
