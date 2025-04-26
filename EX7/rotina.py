import re

class FilaAtendimento:
    def __init__(self) -> list:
        self.clientes: list = []
                
    def adicionar_cliente(self, nome: str):
        self.clientes.append(nome)
    
    def atende_ultimo_cliente(self):
        if self.clientes:
            print(f"\nCliente atendido: {self.clientes[-1]}.")
            self.clientes.pop()
        else:
            print("\nNão há clientes para atendimento")
    
    def exibir_clientes_na_fila(self):
        print("\nClientes na fila:")
        for i, cliente in enumerate(self.clientes, 1):
            print(f"{i} - {cliente}")
        
class InterfaceAtendente:
    def mostrar_menu():
        print('''
        Escolha uma das opções: 
        1 - Adicionar cliente à fila
        2 - Atender próximo cliente(remove da fila)
        3 - Exibir clientes na fila: 
        4 - Sair''')
        
    def obter_opcao():
        entrada_valida: bool = False
        
        while not entrada_valida:
            opcao = input("Opção: ")
            
            if re.search(r'[^1-4]', opcao):
                print("Entrada inválida, Digite uma opção válida!")
                continue
            return int(opcao)
        
class IniciarAtendimento:
    fila = FilaAtendimento()
    terminar_atendimento: bool = False

    while not terminar_atendimento:
        InterfaceAtendente.mostrar_menu()
        opcao = InterfaceAtendente.obter_opcao()
        
        match opcao:
            case 1:
                nome = input("Nome do cliente: ")
                fila.adicionar_cliente(nome)
            case 2:
                fila.atende_ultimo_cliente()
            case 3:
                fila.exibir_clientes_na_fila()
            case 4:
                terminar_atendimento = True