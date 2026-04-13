import re

texto = input("Digite o nome do produto: ")

padrao = r"\w+"

print(re.findall(padrao, texto))