from wsgiref.simple_server import make_server


def aplicacao_web(environ, start_response):  # environ: dicionário com informações da requisição; start_response: função que envia a resposta
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    html = '''
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        <h1>Olá mundo</h1>
    </body>
    </html>
    '''.encode('utf-8')
    return [html]


if __name__ == '__main__':
    server = make_server('', 5000, aplicacao_web)  # host (local), porta, aplicação
    print('Servindo em http://localhost:5000')
    server.serve_forever()