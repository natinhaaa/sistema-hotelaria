################## CLASSE CLIENTE ##################

class Cliente:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.reserva = []

################## GETTERS E SETTERS ##################

    def getReserva(self):
        return self.reserva
    
    def getNome(self):
        return self.nome
    
    def getEmail(self):
        return self.email
    
    def getSenha(self):
        return self.senha
    
################## CLASSE HOTEL ##################

class Hotel:
    def __init__(self):
        self.nomes = [] # Lista de nomes dos clientes
        self.quartos = {"Luxo" : 2 , "Master" : 2 , "Simples" : 3, "Simples Casal" : 3, "Duo" : 3, "Duo Casal" : 3} # Lista de quartos e a quantidade dísponivel
    
    def ListarQuartos(self):
        cont = 0
        for chave, valor in self.quartos.items():
            cont += 1
            print(f"{cont}- {chave}: {valor}")
        
    def Cadastrar(self, nome, email, senha):
        cliente = Cliente(nome, email, senha)
        self.nomes.append(cliente)

    def Login(self, email, senha):
        for cliente in self.nomes:
            if cliente.getEmail() == email  and cliente.getSenha() == senha:
                return 1
            
    def getNomeCliente(self, email):
        for cliente in self.nomes:
            if cliente.getEmail() == email:
                return cliente.getNome()

################## CLASSE QUARTOS ##################

class Quartos(Hotel):

    def ClienteVisualizarReserva(self, email):
        cont = 0
        for cliente in self.nomes:
            if cliente.getEmail() == email:
                for i in cliente.getReserva():
                    cont += 1
                    print(f"{cont} - {i}")
        
    def Cancelar(self, email, vetorQ):
        for cliente in self.nomes:
            if cliente.getEmail() == email:
                self.quartos[cliente.getReserva()[vetorQ -1]] += 1
                cliente.getReserva().pop(vetorQ - 1)
        
    def LuxoCadastro(self, email):
        if self.quartos["Luxo"] <= 2 and self.quartos["Luxo"] > 0:
            for cliente in self.nomes:
                if cliente.getEmail() == email:
                    cliente.getReserva().append("Luxo")
                    self.quartos["Luxo"] -= 1
                    print(f"Quarto de Luxo alugado por {cliente.getNome()}.")
        else:
            print("Indisponível.")

    def MasterCadastro(self, email):
        if self.quartos["Master"] <= 2 and self.quartos["Master"] > 0:
            for cliente in self.nomes:
                if cliente.getEmail() == email:
                    cliente.getReserva().append("Master")
                    self.quartos["Master"] -= 1
                    print(f"Quarto Master alugado por {cliente.getNome()}.")
        else:
            print("Indisponível.")

    def SimplesCadastro(self, email):
        if self.quartos["Simples"]  <= 3 and self.quartos["Simples"]  > 0:
            for cliente in self.nomes:
                if cliente.getEmail() == email:
                    cliente.getReserva().append("Simples")
                    self.quartos["Simples"] -= 1
                    print(f"Quarto simples alugado por {cliente.getNome()}.")
        else:
            print("Indisponível.")

    def SimplesCasalCadastro(self, email):
        if self.quartos["Simples Casal"]  <= 3 and self.quartos["Simples Casal"]  > 0:
            for cliente in self.nomes:
                if cliente.getEmail() == email:
                    cliente.getReserva().append("Simples Casal")
                    self.quartos["Simples Casal"] -= 1
                    print(f"Quarto Simples de Casal alugado por {cliente.getNome()}.")
        else:
            print("Indisponível.")

    def DuoCadastro(self, email):
        if self.quartos["Duo"] <= 3 and self.quartos["Duo"] > 0:
            for cliente in self.nomes:
                if cliente.getEmail() == email:
                    cliente.getReserva().append("Duo")
                    self.quartos["Duo"] -= 1
                    print(f"Quarto duplo alugado por {cliente.getNome()}.")
        else:
            print("Indisponível.")

    def DuoCasalCadastro(self, email):
        if self.quartos["Duo Casal"] <= 3 and self.quartos["Duo Casal"] > 0:
            for cliente in self.nomes:
                if cliente.getEmail() == email:
                    cliente.getReserva().append("Duo Casal")
                    self.quartos["Duo Casal"] -= 1
                    print(f"Quarto Duo de Casal alugado por {cliente.getNome()}.")
        else:
            print("Indisponível.")


recepcionista = Quartos()