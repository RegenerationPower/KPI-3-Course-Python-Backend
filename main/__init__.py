from flask import Flask


app = Flask(__name__)

import main.views

from main.resources import user
from main.resources import notation
from main.resources import category
