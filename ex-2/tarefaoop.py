class Tarefa:
  def __init__(self, tarefa, descricao):
    self.tarefa = tarefa
    self.descricao = descricao
    self._concluida = False

  def __str__(self):
    return f'{self.tarefa:<20} | {self.descricao:<35} | {self.concluida}'

  @property
  def concluida(self):
    return 'Concluída ✅' if self._concluida else 'Pendente ❌'

  def concluir_tarefa(self):
    self._concluida = True

class GerenciadorTarefas:
  def __init__(self):
    self.lista_tarefas = []

  def adicionar_tarefa(self, tarefa):
    self.lista_tarefas.append(tarefa)

  def listar_tarefas(self):
    print(f"{'Tarefa':<20} | {'Descrição':<35} | {'Status'}")
    print("-" * 75)
    for tarefa in self.lista_tarefas:
      print(tarefa)

  def listar_tarefas_pendentes(self):
    print(f"{'Tarefa':<20} | {'Descrição':<35} | {'Status'}")
    print("-" * 75)
    for tarefa in self.lista_tarefas:
      if not tarefa._concluida:
        print(tarefa)

  def remover_tarefa(self, tarefa_para_remover):
    self.lista_tarefas.remove(tarefa_para_remover)
    print('Tarefa apagada do sistema!')

gerenciador = GerenciadorTarefas()

t1 = Tarefa('Estudar Python', 'Estudar Python por 45min')
t2 = Tarefa('Fazer exercícios de POO', 'Estudar POO')
t3 = Tarefa('Descansar a mente', 'Descansar 15min')
t4 = Tarefa('Limpar o carro', 'Lavar o carro sujo')

# Adicionando ao gerenciador
gerenciador.adicionar_tarefa(t1)
gerenciador.adicionar_tarefa(t2)
gerenciador.adicionar_tarefa(t3)
gerenciador.adicionar_tarefa(t4)

# Concluindo apenas uma tarefa
t1.concluir_tarefa()
t2.concluir_tarefa()
t3.concluir_tarefa()

print("\n--- TODAS AS TAREFAS ---\n")
gerenciador.listar_tarefas()

print("\n--- APENAS TAREFAS PENDENTES ---\n")
gerenciador.listar_tarefas_pendentes()