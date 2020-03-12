# myRetail RESTful service

## Build

```bash
make up
```

## Test it

### Manual Tests

`curl` works but I like to use `httpie`

```bash
# start a virtualenv first
virtualenv -p /path/to/python3 .venv
source .venv/bin/activate
# install the library
pip install httpie
```

#### GET requests

See a list of products or a product with a specified `id`.

```bash
http localhost:5000/products
http localhost:5000/products/<id>
```

#### POST requests

Create new products.

```bash
http POST localhost:5000/products < tests/product.json
http POST localhost:5000/products name='my movie 5' current_price='{"value": 12.99}'
```

#### PUT requests

Update an existing product.

```bash
http PUT localhost:5000/products/<id> name="updated product name"
```

#### DELETE requests

Delete an existing product.

```bash
http DELETE localhost:5000/products/<id>
```

### PyRestTest

Set up a virtualenv

```bash
virtualenv -p /path/to/python3 .venv
source .venv/bin/activate
```

Install test requirements

```bash
pip install -r requirements-test.txt
```

Run the tests

```bash
resttest.py http://localhost:5000 tests/rest-test.yml
```

## Clean up

- `CTRL+C` to exit the api container
- Run `docker-compose down`
- If you created a local virtualenv run `deactivate && rm -rf .venv`
