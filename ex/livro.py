class Livro:
    catalogo = []

    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self._disponivel = True
        Livro.catalogo.append(self)

    def __str__(self):
        return f'{self.titulo.ljust(30)} | {self.autor.ljust(20)} | {str(self.ano_publicacao).ljust(10)} | {self.disponivel}'

    @property
    def disponivel(self):
        return '✅' if self._disponivel else '❌'

    def emprestar(self):
        self._disponivel = False

    @classmethod
    def verificar_disponibilidade(cls, ano):
        print(f"\nVerificando disponibilidade para o ano: {ano}")
        livros_encontrados = False
        for livro in cls.catalogo:
            if livro.ano_publicacao == ano:
                print(f"O livro '{livro.titulo}' está {livro.disponivel}")
                livros_encontrados = True
        
        if not livros_encontrados:
            print(f"Nenhum livro encontrado de {ano}.")

# Testando o código
if __name__ == "__main__":
    livro1 = Livro('Entendendo Algoritmos', 'Aditya Y. Bhargava', 2017)
    livro1.emprestar()
    print(livro1)

    livro2 = Livro('Código Limpo', 'Robert C. Martin', 2009)
    print(livro2)

    # Chamando o método de classe
    Livro.verificar_disponibilidade(2017)
    Livro.verificar_disponibilidade(2009)
    Livro.verificar_disponibilidade(2024)