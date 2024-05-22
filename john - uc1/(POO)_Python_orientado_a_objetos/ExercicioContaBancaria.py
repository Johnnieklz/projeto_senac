class ContaBancaria:
    def __init__(self, titular, numero, saldo):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo
            
        
    def Depositar(self):
        valor = float(input("Digite o valor a ser depositado: "))
        self.saldo += valor
        print(f"Seu novo saldo é: {self.saldo}")
        
    def Consultar(self):
        print(f"Seu saldo é: {self.saldo}")
        
    def Transferir(self):
        valor = float(input("Digite o valor a ser transferido: "))
        if saldo < valor:
            print("Saldo insuficiente!")
            return
        self.saldo -= valor
        print(f"Seu novo saldo é: {self.saldo}")
        
    def Sacar(self):
        valor = float(input("Digite o valor a ser sacado: "))
        self.saldo -= valor
        print(f"Seu novo saldo é: {self.saldo}")
        
    def __str__(self):
        return f"\nTitular: {self.titular} \nNumero: {self.numero} \nSaldo: {self.saldo}"
    
   
ClienteUm = ContaBancaria("John" , 123456 , 785.56)
print("Dados Inicias: ", ClienteUm)




