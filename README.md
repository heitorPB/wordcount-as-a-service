# Word Count as a Service

## Usage

There are two REST endpoints for the system:

- `GET /words`: to submit a text string
- `POST /words`: to submit a text file

Both endpoints return a `json` with the word count, for example:

```bash
$ curl http://localhost/words?text=asdf%20asdf
{"words":2}
```

A live Swagger instance is available at [/docs](http://localhost/docs)
endpoint. The OpenAPI Schema is available at
[/openapi.json](http://localhost/openapi.json) and
[/redoc](http://localhost/redoc) provides another viewer for the documentation.


## Running locally

You need a modern Python installation (3.6 or newer) and your favourite library
manager.  Create a virtual environment, install the dependencies, and start it:

```bash
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements
$ cd app
$ uvicorn main:app --reload
```

This will start a web server listening on port `8000`.

Alternatively, you can use the supplied `Dockerfile`:

```bash
# docker build -t wc .
# docker run --publish 80:80 --detach wc
```

The container uses [gunicorn](https://gunicorn.org/) with some auto
configuration options for auto-tunning.


## Deployment

## License

Distributed under the GNU GPLv3. See [LICENSE](LICENSE) for details.
