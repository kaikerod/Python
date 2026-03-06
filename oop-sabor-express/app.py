from modelos.resturante import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebida import Bebida

restaurante_praca = Restaurante('Praça', 'Gourmet')
bebida_suco = Bebida('Suco de Melancia', 5, 'Pequeno')
bebida_suco.aplicar_desconto()
prato_feijoada = Prato('Feijoada', 15, 'Feijoada com arroz')
prato_feijoada.aplicar_desconto()
restaurante_praca.adicionar_item_no_cardapio(bebida_suco)
restaurante_praca.adicionar_item_no_cardapio(prato_feijoada)

def main():
  restaurante_praca.exibir_cardapio

if __name__ == '__main__':
  main()