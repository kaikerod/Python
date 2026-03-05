from modelos.resturante import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebida import Bebida

restaurante_praca = Restaurante('Praça', 'Gourmet')
bebida_suco = Bebida('Suco de Melancia', 5, 'Pequeno')
prato_feijoada = Prato('Feijoada', 15, 'Feijoada com arroz')

def main():
  print(bebida_suco)
  print(prato_feijoada)

if __name__ == '__main__':
  main()