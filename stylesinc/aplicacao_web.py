from wsgiref.simple_server import make_server
import os

def aplicacao_web(environ, start_response):  # environ: dicionário com informações da requisição; start_response: função que envia a resposta
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    
    # Get the directory where the script is located
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, 'index.html')
    
    with open(file_path, 'r', encoding='utf-8') as file:
        html = file.read()
    return [html.encode('utf-8')]


if __name__ == '__main__':
    server = make_server('', 5000, aplicacao_web)  # host (local), porta, aplicação
    print('Servindo em http://localhost:5000')
    server.serve_forever()