FROM nodered/node-red:3.1.5-18
LABEL org.opencontainers.image.base.name="docker.io/library/nodered/node-red:3.1.5-18"
LABEL org.opencontainers.image.authors="kaszpir@gmail.com"
LABEL org.opencontainers.image.description="Node-RED with ffmpeg and Node-RED specific modules installed to allow recording time-lapse videos"
LABEL org.opencontainers.image.url="https://github.com/nvtkaszpir/prusa-esp32-node-red-time-lapse"
LABEL org.opencontainers.image.source="https://github.com/nvtkaszpir/prusa-esp32-node-red-time-lapse"

USER 0
# hadolint ignore=DL3018
RUN apk update \
    && apk add --no-cache \
      ffmpeg \
    && rm /var/cache/apk/*
COPY bin/timelapse.sh /bin/timelapse.sh
USER node-red

# hadolint ignore=DL3016
RUN npm install -u \
    node-red-contrib-counter \
    node-red-contrib-image-output \
    node-red-contrib-moment \
    node-red-contrib-simple-gate \
    node-red-contrib-ui-led \
    node-red-dashboard \
    && ffmpeg -version

ARG GIT_SOURCE
ARG GIT_COMMIT
LABEL org.opencontainers.image.source="${GIT_SOURCE}"
LABEL org.opencontainers.image.revision="${GIT_COMMIT}"
