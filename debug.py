#!/usr/bin/python3

from os import environ as env
env.setdefault('ARGO_SERVER', 'argo.kos.kjnet.xyz')
env.setdefault('ARGO_NAMESPACE', 'default')
env.setdefault('VERSIONS_BACKEND', 'versions.kos.kjnet.xyz')
env.setdefault('MBS_BACKEND', 'mbs.kos.kjnet.xyz')

from front import app
app.jinja_env.auto_reload = True
app.run(debug=True)
