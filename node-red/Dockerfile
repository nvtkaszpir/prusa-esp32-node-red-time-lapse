FROM nodered/node-red
USER 0
RUN apk update \
        && apk add ffmpeg

USER node-red

RUN npm install -u \
    node-red-contrib-file-manager \
    node-red-contrib-image-output \
    node-red-contrib-moment \
    node-red-contrib-ui-led \
    node-red-dashboard
