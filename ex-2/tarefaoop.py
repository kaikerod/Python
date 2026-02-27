class Tarefa:
  def __init__(self, tarefa):
    self.tarefa = tarefa
    self._concluida = False

  def __str__(self):
    return f'{self.tarefa:<25} | {self.concluida}'

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
    for tarefa in self.lista_tarefas:
      print(tarefa)

  def listar_tarefas_pendentes(self):
    for tarefa in self.lista_tarefas:
      if not tarefa._concluida:
        print(tarefa)

gerenciador = GerenciadorTarefas()

t1 = Tarefa('Estudar Python')
t2 = Tarefa('Fazer exercícios de POO')
t3 = Tarefa('Descansar a mente')
t4 = Tarefa('Limpar o carro')

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