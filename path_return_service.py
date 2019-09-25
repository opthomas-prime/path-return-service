from bottle import route, run, request

@route('/:#.*#')
def index():
    return request.fullpath

run(host='0.0.0.0', port=1234)
