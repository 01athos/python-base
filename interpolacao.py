email_tmpl = """
     Olá, %(nome)s
     Tem interesse em comprar %(produto)s?
     Este produto é otimo para resolver %(texto)s
     Clique agora em %(link)s
     Apenas %(quantidade)d disponiveis!
     Preço promocional %(preco).2f
     """

clientes = ["Caio", "Andreia", "Aloha", "Athos"]
for cliente in clientes:
     print( email_tmpl % {"nome": cliente, "produto": "Prancha de surf", "texto": "Surfar Bem", "link": "https://lostsurfboards.com", "quantidade": 3, "preco": 50.6})

