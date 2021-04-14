FROM node:15.5.1-alpine3.12
RUN npm i -g browser-sync
RUN mkdir /app
WORKDIR /app
ENTRYPOINT browser-sync start -s -f --no-notify --host 0.0.0.0 --port 8080
