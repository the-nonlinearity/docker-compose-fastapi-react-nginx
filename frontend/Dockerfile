FROM node:16.13.0

WORKDIR /app

# Install dependencies
COPY package.json /app

RUN yarn install

COPY . .

EXPOSE 3000

CMD [ "yarn", "start" ]