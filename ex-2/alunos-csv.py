import csv

notas_alunos = [{'nome': 'Paula', 'nota': 7.5}, 
                {'nome': 'Joao', 'nota': 4.0}, 
                {'nome': 'Pedro', 'nota': 8.5}]

with open("ex-2/notas_alunos.csv", "a") as f:
  f.write(f"Notas dos alunos: {notas_alunos}\n")

for nota in notas_alunos:
  if float(nota['nota']) >= 7:
    print(nota)