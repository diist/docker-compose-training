import time
import sys
from redis import Redis, ConnectionError


def connect_to_redis(host):
    print "Connecting to redis"
    sys.stdout.flush()

    while True:
        try:
            redis = Redis(host=host, db=0)
            redis.ping()
            print "Connected to redis"
            sys.stdout.flush()
            return redis
        except ConnectionError:
            print "Failed to connect to redis - retrying"
            sys.stdout.flush()
            time.sleep(1)
