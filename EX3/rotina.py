import re

def peganumero(mensagem: str, mensagemerro: str) -> list[int]:
 numeros_inseridos: list[int] = []

 entrada_indesejada: bool = False
    
 while not entrada_indesejada:
  entrada_usuario: str = input(f"{mensagem}: ")
  
  match entrada_usuario:
   case entrada_usuario if re.search(r'[^0-9]', entrada_usuario):
    print(f"\n{mensagemerro}")
    entrada_indesejada = True
   case '':
    continue
   case _:
    numeros_inseridos.append(int(entrada_usuario))
    print(f"Números inseridos: {numeros_inseridos}\n")
    continue
  
  return numeros_inseridos