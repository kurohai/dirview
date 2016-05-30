from flask import Blueprint
from flask import render_template, request, url_for
from flaskapp import *
import utils


blueprint = Blueprint(flasktemplate.appnamed, __name__)

@blueprint.route('/')
def home():
    return render_template('public/index.html')

@blueprint.route('/dir-view/scan/<dirpath>/')
def scan_dir(dirpath):
    results = session.query(Directory).filter(Directory.name == dirpath).first()
    print results
    # dirpath = os.path.join('./', dirpath)
    # dirpath = os.path.abspath(dirpath)
    return '<br>'.join(utils._scan_dir(results.path))

@blueprint.route('/dir-view/dir/add/<dirpath>/')
def add_dir(dirpath):
    print session.query(User).all()

@blueprint.route('/testdb/')
def testdb():
    dirs = session.query(Directory).all()
    print users
    u = list()
    for user in users:
        u.append(user.path)
    print u
    return '<br>'.join(u)
