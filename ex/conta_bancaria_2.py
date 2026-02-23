class ClienteBanco:
    """Representa um cliente do banco com dados pessoais."""

    def __init__(self, nome, idade, cpf, endereco):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.endereco = endereco

    def __str__(self):
        return f'{self.nome} | {self.idade} | {self.cpf} | {self.endereco}'


class ContaBancaria:
    """Representa uma conta bancária vinculada a um cliente."""

    def __init__(self, titular, saldo=0):
        self.titular = titular  # ClienteBanco ou str (nome)
        self.saldo = saldo
        self._ativo = False

    def __str__(self):
        nome_titular = self.titular.nome if isinstance(self.titular, ClienteBanco) else self.titular
        return f'{nome_titular} | R$ {self.saldo:.2f} | {self.ativo}'

    def ativar_conta(self):
        self._ativo = True

    @property
    def ativo(self):
        return '✅' if self._ativo else '❌'


# Uso integrado: cliente → conta
cliente_maria = ClienteBanco('Maria', 30, '111.222.333-44', 'Rua Lisboa')
conta_maria = ContaBancaria(cliente_maria, 1000)
conta_maria.ativar_conta()

cliente_joao = ClienteBanco('João', 25, '555.666.777-88', 'Rua Madrid')
conta_joao = ContaBancaria(cliente_joao, 500)

cliente_kaike = ClienteBanco('Kaike', 20, '1234', 'Rua Bruxelas')
conta_kaike = ContaBancaria(cliente_kaike, 300)
conta_kaike.ativar_conta()

print('--- Contas ---')
print(conta_maria)
print(conta_joao)
print(conta_kaike)
print('\n--- Cliente (exemplo) ---')
print(cliente_kaike)
