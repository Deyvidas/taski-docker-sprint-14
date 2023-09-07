FROM node:18
WORKDIR /app

COPY package.json package.json
COPY package-lock.json package-lock.json

RUN npm install

COPY . .
RUN npm run build

RUN chmod +x collect_frontend_static.sh

CMD /app/collect_frontend_static.sh