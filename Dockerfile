# Build step #1: build the React front end
# pull official base image
FROM node:16.13-alpine as build-step

# set working directory
WORKDIR /app

# add `/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH

# install app dependencies
COPY ./frontend/package.json ./
COPY ./frontend/package-lock.json ./
RUN npm install
RUN npm install react-scripts@4.0.3 -g

COPY ./frontend ./

RUN npm run build

# add app

# start app
CMD ["npm", "start"]

# Build step #2: build the API with the client as static files
FROM python:3.9-alpine
WORKDIR /app
COPY --from=build-step /app/build ./build

RUN mkdir ./backend
COPY backend/ ./backend/
RUN pip install -r ./backend/requirements.txt
ENV FLASK_ENV production

EXPOSE 3000
WORKDIR /app/backend
CMD ["gunicorn", "-b", "0.0.0.0:3000", "wsgi:app"]