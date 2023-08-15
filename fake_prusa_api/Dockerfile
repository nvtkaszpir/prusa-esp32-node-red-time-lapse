FROM python:3.10
LABEL org.opencontainers.image.base.name="docker.io/library/python:3.10"
LABEL org.opencontainers.image.authors="kaszpir@gmail.com"
LABEL org.opencontainers.image.description="Basic python app with flask to simulate Prusa Mini+ web API (Prusa Connect)"
LABEL org.opencontainers.image.url="https://github.com/nvtkaszpir/prusa-esp32-node-red-time-lapse"
LABEL org.opencontainers.image.source="https://github.com/nvtkaszpir/prusa-esp32-node-red-time-lapse"

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
USER nobody

CMD [ "flask", "run", "--host", "0.0.0.0", "--debug" ]
EXPOSE 5000/tcp

HEALTHCHECK CMD curl -f http://localhost:5000/health || exit 1
