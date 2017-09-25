FROM node
WORKDIR /app
COPY rldb/package.json .
ENV PATH /app/node_modules/.bin:$PATH
RUN npm install
CMD npm start
