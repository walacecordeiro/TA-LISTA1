import rotinas
import re

numeros: list[int] = []

VARIAVEL_CONTROLE: int = 0

print("Se você digitar o número '0' a lista termina e executa as rotinas")
while VARIAVEL_CONTROLE not in numeros:
    entrada_usuario: str = input("Adicione um número: ")
    remove_caracteres_indesejados: str = re.sub(r'[^0-9]', '', entrada_usuario)
    
    if remove_caracteres_indesejados == '':
        continue # Se True, volta direto ao início do loop
    else:
        conversao: int = int(remove_caracteres_indesejados)
        numeros.append(conversao)
    
numeros.pop()   
    
if len(numeros) > 1:
    rotinas.calculos(numeros)
    rotinas.duplicados(numeros)
    rotinas.impares_e_pares_distintos(numeros)
    rotinas.numeros_primos(numeros)
elif len(numeros) == 1:
    print("É necessário ao menos dois números, reinicie o programa!")
else:
    print("Não há dados para executar as operações, programa encerrado!")