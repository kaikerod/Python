from modelos.resturante import Restaurante

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Kaike', 5)
restaurante_praca.receber_avaliacao('Maria', 4)
restaurante_praca.receber_avaliacao('Emy', 7)
restaurante_praca.receber_avaliacao('Eva', 10)

# restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
# restaurante_japones = Restaurante('Sushi', 'Japonesa')

def main():
  Restaurante.listar_restaurantes()

if __name__ == '__main__':
  main()