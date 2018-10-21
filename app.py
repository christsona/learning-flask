from flask import Flask, render_template
app = Flask(__name__)

from config import *
from home import *
from about import *


if __name__ == "__main__":
    app.secret_key = 'Secret key'
    app.run(debug = True)
