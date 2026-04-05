import os
from flask import Flask, render_template
import redis

app = Flask(__name__)
redis_host= os.getenv('REDIS_HOST','redis')
redis_port= int(os.getenv('REDIS_PORT',6379))
r = redis.Redis(host=redis_host, port=redis_port)

@app.route('/')
def welcome():
    return render_template('home.html')

@app.route('/count')
def count():
    visits = r.incr('visits')
    return render_template('visits.html', count=visits)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
        app.run(host='0.0.0.0',port=5001)
