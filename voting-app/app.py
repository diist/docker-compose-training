from flask import Flask
from flask import render_template
from flask import request
from flask import make_response
from lib import utils
import os
import socket
import random
import json
import sys

print "\nWeb App Starting..."

option_a = os.getenv('OPTION_A', "Cats")
option_b = os.getenv('OPTION_B', "Dogs")
redis_host = os.getenv('REDIS_HOST', "localhost")
hostname = socket.gethostname()

redis = utils.connect_to_redis(redis_host)
app = Flask(__name__)

print "Listening on port 5000..."
sys.stdout.flush()

@app.route("/", methods=['POST','GET'])
def hello():
    count_a = redis_get_int('a')
    count_b = redis_get_int('b')
    
    vote = None
    if request.method == 'POST':
        vote = request.form['vote']
        print "Inserting a vote for option {0} in Redis!".format(vote)
        sys.stdout.flush()
        if vote == 'a':
            count_a += 1
            redis.set('a', count_a)
        elif vote == 'b':
            count_b += 1
            redis.set('b', count_b)

    resp = make_response(render_template(
        'index.html',
        option_a=option_a,
        count_a=count_a,
        option_b=option_b,
        count_b=count_b,
        hostname=hostname,
        vote=vote,
    ))
    return resp

def redis_get_int(option):
    option_str = redis.get(option)
    return 0 if not option_str else int(option_str)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
