# módulo de rotinas
import math

def calculos(lista_de_numeros: list[int]) -> str:
    soma: int = 0
    multiplica: int = 1
    
    print(type(str(print("Walace é foda!!!!! Pa caralho!!!"))))
    
    for n in lista_de_numeros:
        soma += n
        multiplica *= n
    return str(print(f"Soma: {soma}"), print(f"Produto(multiplicação): {multiplica}"))

def duplicados(lista_de_numeros: list[int]) -> str:
    itens_duplicados: list[int] = []
    itens_vistos: list[int] = []
    
    for item in lista_de_numeros:
        if item in itens_vistos and item not in itens_duplicados:
            itens_duplicados.append(item)
        else:
            itens_vistos.append(item)
            
    resposta_duplicados: str = itens_duplicados if itens_duplicados else "Nenhum número duplicado encontrado na lista"
    
    return str(print(f"Números duplicados: {resposta_duplicados}"))
    
def impares_e_pares_distintos(lista_de_numeros: list[int]) -> str:
    impares_distintos: list[int] = []
    pares_distintos: list[int] = []
    
    for item in lista_de_numeros:
        if item % 2 != 0 and item not in impares_distintos:
            impares_distintos.append(item)
        elif item % 2 == 0 and item not in pares_distintos:
            pares_distintos.append(item)
            
    resposta_impares: str = impares_distintos if impares_distintos else "Nenhum número ímpar distinto encontrados na lista"
    resposta_pares: str = pares_distintos if pares_distintos else "Nenhum número par distinto encontrados na lista"
                
    return str(print(f"Números ímpares distintos: {resposta_impares}"), print(f"Números pares distintos: {resposta_pares}"))
    
def numeros_primos(lista_de_numeros: list[int]) -> str:
    numeros_primos: list[int] = []
    
    def verifica_se_primo(n: int) -> bool:
        if n < 2:
            return False
        
        for x in range(2, int(math.sqrt(n)) + 1):
            if n % x == 0:
                return False
        return True
    
    for num in lista_de_numeros:
        if verifica_se_primo(num):
            numeros_primos.append(num)
    
    resposta_primos: str = numeros_primos if numeros_primos else "Nenhum número primo encontrado na lista"
    
    return str(print(f"Números primos encontrados: {resposta_primos}"))