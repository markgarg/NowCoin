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
app = Flask(__name__)

@app.route("/",  methods=['GET','POST'])
def index():
    resp = make_response(render_template('index.html'), 200)
    if request.method == 'POST':
        cost = request.form['cost']
        print(cost)
    return resp


@app.route("/users",  methods=['GET'])
def users():
    resp = make_response(render_template('users.html'), 200)
    return resp


# runs app when called
def apprun():
    app.run(host='0.0.0.0', threaded=True, debug=True)

# runs the flask web app
if __name__ == '__main__':
    apprun()