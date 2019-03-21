"""
All rest call related code will reside here.
It includes, wrapper for rest operations and error handling.
Schema validation, configuration options and authentication methods.
"""
import flask
from tradingPlatform.flaskapp import app
from tradingPlatform import api


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


