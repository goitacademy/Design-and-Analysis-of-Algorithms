import redis
from redis_lru import RedisLRU

client = redis.StrictRedis(host="localhost", port=6379, password=None)
cache = RedisLRU(client)


@cache
def f(x):
    print(f"Function call f({x})")
    return x


if __name__ == "__main__":
    print(f"Result f(3): {f(3)}")
    print(f"Result f(3): {f(3)}")
