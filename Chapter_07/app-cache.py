import redis
import json
import uvicorn
from fastapi import FastAPI

app = FastAPI()
# Connecting to Redis
r = redis.Redis(host="localhost", port=6379, db=0)

database = {"10": 10, "11": 11, "12": 12}


@app.get("/product/{product_id}")
def read_product(product_id: int):
    product = r.get(str(product_id))
    if product is None:
        product = fetch_product_from_db(product_id)
        r.set(str(product_id), json.dumps(product))
        r.expire(str(product_id), 3600)
        return product
    return json.loads(product)


def fetch_product_from_db(product_id: int):
    data = database.get(str(product_id), None)
    print(f"Fetching from DB {product_id}")
    return data


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
