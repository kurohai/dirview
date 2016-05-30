#!/bin/env python

from flask import Flask


flasktemplate = Flask(__name__)
flasktemplate.appname = 'Flask Template'
flasktemplate.appnamed = 'flasktemplate'
flasktemplate.config.SECRET_KEY = 'enydM2ANhdcoKwdVa0jWvEsbPFuQpMjf'
flasktemplate.config.SESSION_PROTECTION = 'strong'



@flasktemplate.template_global()
def appname():
    return flasktemplate.appname


@flasktemplate.template_global()
def appnamed():
    return flasktemplate.appnamed


@flasktemplate.errorhandler(404)
def error_not_found(error):
    """Render a custom template when responding with 404 Not Found."""
    return 'No page here, dood. 404!', 404
