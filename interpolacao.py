import sys
import os

arguments = sys.argv[1:]
if not arguments:
    print("informe o nome do arquivo de emails")
    sys.exit(1)

filename = arguments[0]

path = os.curdir
filepath = os.path.join(path, filename)

clientes = []
for line in open(filepath):
    clientes.append(line.split(","))

email_tmpl = """
     Olá, %(nome)s
     Tem interesse em comprar %(produto)s?
     Este produto é otimo para resolver %(texto)s
     Clique agora em %(link)s
     Apenas %(quantidade)d disponiveis!
     Preço promocional %(preco).2f
     Email %(email).2f
     """

for name, email in clientes:
    print(f"Enviando email para: {email}")
    print( email_tmpl % {"nome": name, "produto": "Prancha de surf", "texto": "Surfar Bem", "link": "https://lostsurfboards.com", "quantidade": 3, "preco": 50.6})
    print("-" * 50)
