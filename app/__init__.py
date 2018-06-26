from flask import Flask

app = Flask('HW')
app.config.from_object('config')

from app import views
