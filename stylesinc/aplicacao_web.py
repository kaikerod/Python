from wsgiref.simple_server import make_server

def aplicacao_web(environ, start_response): # 
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return [b'Hello World']

make_server('', 5000, 'aplicacao_web') # host (local), porta, aplicação