FROM node
WORKDIR /app
COPY rldb/package.json .
ENV NPM_CONFIG_LOGLEVEL warn
ENV PATH /app/node_modules/.bin:$PATH
RUN npm install
CMD CHOKIDAR_USEPOLLING=true npm start
