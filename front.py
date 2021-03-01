#!/usr/bin/python3

from flask import Flask
from flask import render_template
from flask import abort

from data import DAO
dao = DAO()

app = Flask('mbs-front', template_folder='templates',
            static_folder='static',
            static_url_path='/static')

#app.config.update(get_config('flask'))
#from werkzeug.middleware.proxy_fix import ProxyFix
#app.wsgi_app = ProxyFix(app.wsgi_app)

last_id = 0
def next_id(prefix='id'):
    global last_id
    last_id += 1
    return f"{prefix}-{last_id}"

import rpm
def version_compare(left: str, right: str) -> int:
    return rpm.labelCompare(("", left, ""), ("", right, ""))


app.jinja_env.globals.update(
    states=['Pending','Running', 'Succeeded', 'Failed', 'Error'],
    next_id=next_id,
    version_compare=version_compare,
)


@app.route('/')
def list_builds():
    return render_template(
        'list-builds.html',
        builds=dao.builds,
    )


@app.route('/build/<id>')
def build_details(id):
    builds = dao.builds
    for build in builds:
        if build.id == id:
            break
    else:
        abort(404)
    return render_template(
        'build-details.html',
        build=build,
        builds=builds,
    )

@app.route('/versions')
def versions_dashboard():
    versions = dao.versions
    return render_template(
        'versions.html',
        report_dict=versions,
    )
