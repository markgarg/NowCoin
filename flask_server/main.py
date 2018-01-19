import time
from flask import (
    Flask,
    request,
    url_for,
    redirect,
    make_response,
    render_template,
    jsonify
)
from tasks import my_background_task
from celery import Celery

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

@app.route("/",  methods=['GET'])
def index():
    resp = make_response(render_template('index.html'), 200)
    return resp

@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404

@app.route("/task",  methods=['POST'])
def add_task():
    task = my_background_task.delay("Puppies")
    print("Added: %s to the queue" % task.id)
    return task.id

@app.route("/status/<task_id>", methods=['GET'])
def task_status(task_id):
    task = my_background_task.AsyncResult(task_id)
    if task.state == "PENDING":
        response = "PENDING"
    elif task.state == "FAILURE":
        response = "FAILURE"
    elif task.state == "SUCCESS":
        response = "SUCCESS"
    else:
        response = "Something went wrong..."
    return jsonify(response)
