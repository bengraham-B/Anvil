from flask import Flask, Blueprint
from controllers.test import test

blueprint = Blueprint('blueprint', __name__)

blueprint.route('/', methods=["GET"])(test)
