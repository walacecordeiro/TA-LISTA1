# módulo de rotinas
import math

def calculos(lista_de_numeros: list[int]) -> str:
    resultado_soma: int = 0
    resultado_multiplicacao: int = 0
    
    def soma(lista: list[int]) -> int:
        if not lista:
            return 0
        
        primeiro_valor = lista[0]
        soma_restante = soma(lista[1:])
        return primeiro_valor + soma_restante
    
    def multiplicacao(lista: list[int]) -> int:
        if not lista:
            return 1
        
        primeiro_valor = lista[0]
        soma_restante = multiplicacao(lista[1:])
        return primeiro_valor * soma_restante
    
    resultado_soma = soma(lista_de_numeros)
    resultado_multiplicacao = multiplicacao(lista_de_numeros)
    
    resultado: str = f"Soma: {resultado_soma}\nProduto(multiplicação): {resultado_multiplicacao}"
    
    return resultado

def duplicados(lista_de_numeros: list[int]) -> str:
    itens_duplicados: list[int] = []
    itens_vistos: list[int] = []
    
    def recursao_duplicados(lista: list[int]) -> None:
        if not lista:
            return 0
        
        primeiro_valor = lista[0]
        
        if primeiro_valor in itens_vistos and primeiro_valor not in itens_duplicados:
            itens_duplicados.append(primeiro_valor)
        else:
            itens_vistos.append(primeiro_valor)
            
        recursao_duplicados(lista[1:])
        
    recursao_duplicados(lista_de_numeros)
    
    existe_ou_nao_duplicados: str = itens_duplicados if itens_duplicados else "Nenhum número duplicado encontrado na lista"
    resposta: str = f"Números duplicados: {existe_ou_nao_duplicados}"
    
    return resposta
    
def impares_e_pares_distintos(lista_de_numeros: list[int]) -> str:
    impares_distintos: list[int] = []
    pares_distintos: list[int] = []
    
    def recursao_impares_pares_distintos(lista: list[int]) -> None:
        if not lista:
            return 0
        
        primeiro_valor = lista[0]
        
        if primeiro_valor % 2 != 0 and primeiro_valor not in impares_distintos:
            impares_distintos.append(primeiro_valor)
        elif primeiro_valor % 2 == 0 and primeiro_valor not in pares_distintos:
            pares_distintos.append(primeiro_valor)
            
        recursao_impares_pares_distintos(lista[1:])
        
    recursao_impares_pares_distintos(lista_de_numeros)
    
    resposta_impares: str = impares_distintos if impares_distintos else "Nenhum número ímpar distinto encontrados na lista"
    resposta_pares: str = pares_distintos if pares_distintos else "Nenhum número par distinto encontrados na lista"
    
    retorno: str = f"Números ímpares distintos: {resposta_impares}\nNúmeros pares distintos: {resposta_pares}"
                
    return retorno
    
def numeros_primos(lista_de_numeros: list[int]) -> str:
    numeros_primos: list[int] = []
    
    def verifica_se_primo(n: int) -> bool:
        if n < 2:
            return False
        
        for x in range(2, int(math.sqrt(n)) + 1):
            if n % x == 0:
                return False
        return True
    
    def recursao_numeros_primos(lista: list[int]) -> None:
        if not lista:
            return 0
        
        primeiro_valor: int = lista[0]
        
        if verifica_se_primo(primeiro_valor):
            numeros_primos.append(primeiro_valor)
        
        recursao_numeros_primos(lista[1:])
    
    recursao_numeros_primos(lista_de_numeros)
    
    existe_primos_ou_nao: str = numeros_primos if numeros_primos else "Nenhum número primo encontrado na lista"
    resposta_primos: str = f"Números primos encontrados: {existe_primos_ou_nao}"
    
    return resposta_primos