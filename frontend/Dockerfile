FROM node:18
WORKDIR /app

COPY package.json /app/package.json
COPY package-lock.json /app/package-lock.json

RUN npm install

COPY . .

RUN npm run build

CMD npx -y http-server -p 8000 /app/build/