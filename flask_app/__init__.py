from flask import Flask
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "736d51f0a219f30b0a6dc7d1a8ffa5d34934d2bdc72d440f8ee81b7f88a8e898"
