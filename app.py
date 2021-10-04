import os
from flask import Flask, request, jsonify
from rq import Queue
from worker import conn
from utils import scrapeAnswer
import json
from time import sleep

app = Flask(__name__)
q = Queue(connection=conn)

def get_status(job):
    return 'Your API request failed for some reason :(' if job.is_failed else 'your API is pending, please wait' if job.result == None else job.result

@app.route("/")
def handle_job():
    qq = request.args.get('q')
    if qq:
        job = q.enqueue(scrapeAnswer, qq)
        while job.result == None:
            sleep(0.1)
        else:
            output = get_status(job)
    else:
        return "Cannot GET"
    return output

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)