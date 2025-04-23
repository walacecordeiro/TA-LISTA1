from rotina import peganumero

numeros_coletados: list[int] = peganumero("Insira um número", "Erro: apenas números são aceitos, programa encerrado!")

print(f"Números enviados: {numeros_coletados}\n")