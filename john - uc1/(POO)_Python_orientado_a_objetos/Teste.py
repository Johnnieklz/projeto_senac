'''
titular = []
numero = []

nome = str(input("Digite o nome do titular da conta: "))
numConta = int(input("Digite o número do titular da conta: "))    
    
class Conta_Bancaria:
    def __init__(self, titular, numero, saldo):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo
        
    def depositar(self, valor):
        valor = float(input("Digite o valor a ser depositado: "))
        self.saldo += valor
        print(f"O valor de {valor} foi depositado com sucesso!")
        
    def sacar(self, valor):
        valor = float(input("Digite o valor a ser sacado: "))
        if self.saldo < valor :
            print("Saldo insuficiente! ")            
        else:
            self.saldo -= valor
            print(f"O valor de {valor} foi sacado com sucesso!")
        
        self.saldo -= valor
        print(f"O valor de {valor} foi sacado com sucesso!")
        
    def consultar(self):
        print(f"O saldo atual é de {self.saldo}")
        
    def tranferir(self):
        valor = float(input("Digite o valor a ser transferido: "))
        self.saldo -= valor
        print(f"O valor de {valor} foi transferido com sucesso!")
        
    def __str__(self):
        return f"Titular: {self.titular}\nNúmero: {self.numero}\nSaldo: {self.saldo}"
          
        
ClienteUm = Conta_Bancaria(titular=nome, numero=numConta, saldo=753.56)         
print("Dados:", ClienteUm)    
 '''   
    
# ==================================================================== #   
    
#                                 Resposta
    
# ==================================================================== #


class ContaBancaria:
    def __init__(self, nome_titular, numero_conta, saldo_inicial=0):
        self.nome_titular = nome_titular
        self.numero_conta = numero_conta
        self.saldo_inicial = saldo_inicial
        
    def depositar(self, valor):
        if valor < 0:
            print("Valor de depósito inválido!")
        else: 
            self.saldo_inicial += valor
            print(f"Depósito de R$ {valor} realizado com sucesso!")
    
    def sacar(self, valor):
        if valor > 0:
            if self.saldo >= valor:
                self.saldo -= valor
            else:
                print("Saldo insuficiente!")
        else:
            print("Valor de saque inválido!")
            
    def consultar_saldo(self):
        return self.saldo 
    
    def transferir(self, valor, conta_destino):
        if valor > 0:
            if self.saldo >= valor:
                self.saldo -= valor
                conta_destino.depositar += (valor)
                print("Tranfência feita com sucesso!")
            else:
                print("Saldo insuficiente!")
        else:
            print("Valor de transferência inválido!")
        
    