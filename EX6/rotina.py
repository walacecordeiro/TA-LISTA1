import re

class FilaAtendimento:
    def __init__(self) -> list:
        self.clientes: list = []
                
    def adicionar_cliente(self):
        cliente: str = input("\nInforme o nome do cliente: ")
        self.clientes.append(cliente)
        self.fila_atendimento()
    
    def atender_cliente(self):
        cliente: str = input("\nInforme o nome do cliente: ")
        if cliente in self.clientes:
            self.clientes.remove(cliente)
            self.fila_atendimento()
        else:
            print("\nCliente não está na fila")
            self.fila_atendimento()
    
    def exibir_clientes_na_fila(self):
        print(f"\n{self.clientes}")

    def fila_atendimento(self) -> int:
        opc_selecionada = input('''
        Escolha uma das opções: 
        1 - adicionar cliente à fila
        2 - atender cliente(remover da fila)
        3 - exibir clientes na fila: ''')
        
        match opc_selecionada:
            case opc_selecionada if re.search(r'[^1-3]', opc_selecionada):
                print("\n\t\tInsira uma opção válida!!!")
                self.fila_atendimento()
            case "1":
                self.adicionar_cliente()
            case "2":
                self.atender_cliente()
            case "3":
                self.exibir_clientes_na_fila()