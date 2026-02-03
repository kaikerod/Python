class Livro:
  def __init__(self, titulo, autor, paginas):
    self.titulo = titulo
    self.autor = autor
    self.paginas = paginas

  def __str__(self):
    return f'{self.titulo} | {self.autor} | {self.paginas}'

class Biblioteca:
  def __init__(self):
    self.livros = []

  def adicionar_livro(self, livro):
    self.livros.append(livro)

  def listar_livros(self):
    for livro in self.livros:
      print(livro)

minha_biblioteca = Biblioteca()
livro1 = Livro('Entendendo Algoritmos', 'Aditya Y. Bhargava', 264)
minha_biblioteca.adicionar_livro(livro1)

livro2 = Livro('Código Limpo', 'Robert C. Martin', 425)
minha_biblioteca.adicionar_livro(livro2)
minha_biblioteca.listar_livros()