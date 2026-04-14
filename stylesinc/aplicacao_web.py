from wsgiref.simple_server import make_server

make_server('', 5000, 'aplicacao_web') # host (local), porta, aplicação