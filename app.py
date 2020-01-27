from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/packaging'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "universe"

db = SQLAlchemy(app)
