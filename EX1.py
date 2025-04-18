numeros: list[int] = []
# soma: int = 0

VARIAVEL_CONTROLE: str = 0

print("Se você digitar o número '0' o programa executa as operações")
while VARIAVEL_CONTROLE not in numeros:
    numeros.append(int(input("Adicione um número: "))) # converte a entrada diretamente pois vamos trabalhar apenas com números.
    
numeros.pop()

def calculos(lista_de_numeros: list[int]):
    soma: int = 0
    multiplica: int = 1
    
    if not lista_de_numeros:
        print("Não há dados para calcular, fim do programa")
        return
    else:
        for n in lista_de_numeros:
            soma += n
            multiplica *= n
        return print(f"Soma: {soma}"), print(f"Produto(multiplicação): {multiplica}")

def duplicados(lista_de_numeros: list[int]):
    itens_duplicados: list[int] = []
    itens_vistos: list[int] = []
    
    for item in lista_de_numeros:
        if item in itens_vistos and item not in itens_duplicados:
            itens_duplicados.append(item)
        else:
            itens_vistos.append(item)
            
    if itens_duplicados:        
        return print(f"Números duplicados {itens_duplicados}")
    else:
        return print("Não houve números duplicados")
    
def impares_e_pares_distintos(lista_de_numeros: list[int]):
    impares_distintos: list[int] = []
    pares_distintos: list[int] = []
    
    for item in lista_de_numeros:
        if item % 2 != 0 and item not in impares_distintos:
            impares_distintos.append(item)
        elif item % 2 == 0 and item not in pares_distintos:
            pares_distintos.append(item)
    
    return print(f"Números ímpares distintos: {impares_distintos}"), print(f"Números pares distintos: {pares_distintos}")
    
if len(numeros) > 1:    
    # calculos(numeros)
    # duplicados(numeros)
    impares_e_pares_distintos(numeros)   
elif len(numeros) == 1:
    print("É necessário ao menos dois números, programa encerrado!")
else:
    print("Não há dados para executar as operações, programa encerrado!")