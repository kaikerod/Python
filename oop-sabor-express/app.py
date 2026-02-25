from modelos.resturante import Restaurante

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
restaurante_japones = Restaurante('Sushi', 'Japonesa')

restaurante_japones.alternar_estado()

def main():
  Restaurante.listar_restaurantes()

if __name__ == '__main__':
  main()