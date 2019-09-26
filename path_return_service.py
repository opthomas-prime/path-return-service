import os

from bottle import route, run, request

@route('/:#.*#')
def index():
    if 'SERVICE_NAME' in os.environ:
        service_name = os.environ['SERVICE_NAME']
        return '%s: %s' % (service_name, request.fullpath)
    return '%s' % request.fullpath

run(host='0.0.0.0', port=1234)
