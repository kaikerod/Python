class ContaBancaria:
  def __init__(self, titular, saldo):
    self.titular = titular
    self.saldo = saldo

  def depositar(self, valor):
    self.saldo += valor

  def sacar(self, valor):
    if self.saldo < valor:
      print('Saldo Insuficiente!')
    else:
      self.saldo -= valor
      print('Valor sacado!')

  def consultar_saldo(self):
    print(f'O valor disponível é de R$ {self.saldo}')

cliente1 = ContaBancaria('Cliente A', 1000)
cliente1.sacar(500)
cliente1.consultar_saldo()