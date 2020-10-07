import os
import json

from bottle import route, run, request

@route('/:#.*#')
def index():
    host_header_info = ""
    for header in request.headers.items():
        if "host" in header[0].lower() or "forwarded" in header[0].lower():
            host_header_info = "%s%s: %s\n" % (host_header_info, header[0], header[1])
    if 'SERVICE_NAME' in os.environ:
        service_name = os.environ['SERVICE_NAME']
        return '%s%s: %s\n%s' % (host_header_info, service_name, request.fullpath, json.dumps(request.params.dict))
    return '%s%s\n%s' % (host_header_info, request.fullpath, json.dumps(request.params.dict))

run(host='0.0.0.0', port=1234)
