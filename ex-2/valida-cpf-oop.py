class ValidadorCPF:
  def __init__(self, cpf):
    self.cpf = cpf

  def validar(self):
    if not self.cpf.isdigit():
      return "Erro: O CPF deve conter apenas números."
    if len(self.cpf) != 11:
      return "Erro: O CPF deve ter exatamente 11 dígitos."
    return "CPF válido."

validador = ValidadorCPF("12345678901")
print(validador.validar())