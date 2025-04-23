from re import search

def ano_bissexto_ou_nao() -> str:
    ano_para_verificar: int = 0
    
    while ano_para_verificar == 0:
        entrada_usuario: str = input("Qual ano deseja verificar se é Bissexto? ")
    
        if search(r'[^0-9]', entrada_usuario):
            print("Insira apenas números inteiros!!")
            continue
        else:
            ano_para_verificar = int(entrada_usuario)
        
    verifica_se_bissexto: bool = ano_para_verificar % 400 == 0 or ano_para_verificar % 4 == 0 and ano_para_verificar % 100 != 0
    
    resposta: str = f"{ano_para_verificar} é bissexto." if verifica_se_bissexto else f"{ano_para_verificar} não é bissexto."
    
    print(resposta)
    
ano_bissexto_ou_nao()