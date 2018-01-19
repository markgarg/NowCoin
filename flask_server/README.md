# Flask with Integrated Celery
Using celery to queue API Endpoint service tasks

This Flask application includes API endpoints to provide background tasks to be run. 

The tasks are processed using the multiprocessing capabilities of the python module **Celery**. 

**Redis** is used as a broker to mediate between the clients and worker and as a backend to store the results for gathering at a later time.

### Technologies 

- Flask 
- Celery 
- React 
- Materialize
- Redis

---
## How to setup 

Ensure redis is setup. For Mac Users: 

```
brew install redis
brew services start redis
```

In the terminal, go to a suitable directory (e.g Documents, Desktop) and run the following commands: 

```
git clone https://github.com/Jimmycheong/flask-celery-demo.git
cd flask-celery-demo-master

virtualenv env 
source env/bin/activate 
pip install -r requirements.txt 
```
Run the celery server:
- The -A flag refers to the modules where the celery tasks are defined. 
- The -l flag refers to log level 

```
celery worker -A tasks -l info
```

On another terminal tab, activate the virtual environment, create environment variables and run the Flask application: 
```
source env/bin/activate
export FLASK_APP=main.py
export FLASK_DEBUG=1

flask run

```

Enjoy!

![screen shot 2017-10-10 at 22 17 54](https://user-images.githubusercontent.com/22529514/31411242-e85c99d6-ae08-11e7-9358-c0c80de9b836.jpg)


Awesome references:
- https://github.com/miguelgrinberg/flask-celery-example
