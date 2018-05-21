""" initializing app """
import flask
import views

app = flask.Flask(__name__)
app.config.from_object('config')
