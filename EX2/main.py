import rotinas
import re

numeros: list[int] = []

print("Se você digitar o número '0' as rotinas são executadas")
        
def controle_de_entrada_do_usuário():
    entrada_usuario: str = input("Adicione um número: ")
           
    match entrada_usuario:
        case entrada_usuario if re.search(r'[^0-9]', entrada_usuario) or entrada_usuario == '':
            print("Insira apenas números inteiros!")
            return controle_de_entrada_do_usuário() # Recurção caso entrada indesejada.
        case '0':
            return # Finaliza as entradas
        case _:
            conversao: int = int(entrada_usuario)
            numeros.append(conversao)
            controle_de_entrada_do_usuário() # Recurção acontece para pedir nova entrada do usuário.

controle_de_entrada_do_usuário()  
    
if len(numeros) > 1:
    print(f"\n{rotinas.calculos(numeros)}")
    print(rotinas.duplicados(numeros))
    print(rotinas.impares_e_pares_distintos(numeros))
    print(f"{rotinas.numeros_primos(numeros)}\n")
elif len(numeros) == 1:
    print("É necessário ao menos dois números, reinicie o programa!")
else:
    print("Não há dados para executar as operações, programa encerrado!")