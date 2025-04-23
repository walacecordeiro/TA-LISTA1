from rotina import peganumero

numero_enviado: int = 0

numero_enviado = peganumero("Insira um número", "Erro: letras não são aceitas! apenas número!", 5, 10)

print(f"\nNúmero aceito: {numero_enviado}\n")