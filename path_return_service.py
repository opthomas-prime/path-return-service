import os
import json

from bottle import route, run, request

@route('/:#.*#')
def index():
    if 'SERVICE_NAME' in os.environ:
        service_name = os.environ['SERVICE_NAME']
        return '%s: %s\n%s' % (service_name, request.fullpath, json.dumps(request.params.dict))
    return '%s\n%s' % (request.fullpath, json.dumps(request.params.dict))

run(host='0.0.0.0', port=1234)
