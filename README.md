# hello-python

A tiny Python HTTP server for experimenting with Dockerfiles. It uses only the
Python standard library.

## Run locally

```sh
python app.py
```

Open <http://localhost:8000>.

## Build and run with Docker

```sh
docker build -t hello-python .
docker run --rm -p 8000:8000 hello-python
```

Set a different listening port with the `PORT` environment variable. When
running in Docker, publish the same container port:

```sh
docker run --rm -e PORT=8080 -p 8080:8080 hello-python
```
