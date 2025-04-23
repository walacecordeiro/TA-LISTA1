import re

def peganumero(mensagem: str, mensagem_erro: str, menor_valor: int, maior_valor: int) -> int:
    numero_certo: int = 0

    entrada_indesejada: bool = False
        
    while not entrada_indesejada or numero_certo == 0:
        print(f"\nInsira um número entre {menor_valor} e {maior_valor}")
        entrada_usuario: str = input(f"{mensagem}: ")
            
        match entrada_usuario:
            case entrada_usuario if re.search(r'[^0-9]', entrada_usuario):
                print(f"\n{mensagem_erro}")
                entrada_indesejada = True
                continue
            case '':
                continue
            
        entrada_usuario = int(entrada_usuario)
            
        if entrada_usuario >= menor_valor and entrada_usuario <= maior_valor:
            numero_certo = entrada_usuario
            break
        else:
            print(f"\nNúmero {entrada_usuario} não aceito! precisa ser entre {menor_valor} e {maior_valor}!")
            continue
 
    return numero_certo
 