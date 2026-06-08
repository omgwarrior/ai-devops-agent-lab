import os
import redis

redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=int(os.getenv("REDIS_PORT", "6379")),
    decode_responses=True,
)

def save_memory(key: str, value: str):
    redis_client.set(key, value)

def get_memory(key: str):
    return redis_client.get(key)
