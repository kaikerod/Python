class Cliente:
  def __init__(self, nome, email, plano):
    self.nome = nome
    self.email = email
    self.lista_planos = ['Basic', 'Premium']
    if plano in self.lista_planos:
      self.plano = plano
    else:
      raise Exception ('Plano Inválido!')

  def mudar_plano(self, novo_plano):
    if novo_plano in self.lista_planos:
      self.plano = novo_plano
    else:
      print('Plano Inválido!')

cliente = Cliente('Kaike', 'kaike@gmail.com', 'Basic')
print(cliente.plano)
cliente.mudar_plano('Premium')
print(cliente.plano)