# myRetail RESTful service

## Build

```bash
make up
```

## Test it

### Manual Tests

`curl` works but I like to use `httpie`

```bash
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
http POST localhost:5000/products < product.json
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
