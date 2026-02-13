class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self.categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self.categoria}'

    def listar_restaurantes():
        print(f'{'Nome do restaurante'.ljust(10)} | {'Categoria'.ljust(10)} | {'Status'}\n')
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante._nome.ljust(10)} | {restaurante.categoria.ljust(10)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return '✅' if self._ativo else '❌'

restaurante_praca = Restaurante('Praça', 'Gourmet')
    restaurante_pizza = Restaurante('Pizza Express', 'Italiana')

Restaurante.listar_restaurantes()