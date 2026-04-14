from wsgiref.simple_server import make_server

def aplicacao_web(environ, start_response): # environ: dicionário com informações da requisição, start_response: função que envia a resposta
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    html = b'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
  
    </body>
    </html>
    '''

make_server('', 5000, 'aplicacao_web') # host (local), porta, aplicação