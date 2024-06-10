import sqlite3

class Banco_do_Jurandi:
    def __init__(self, nome_banco = 'Jurandi.db'):
        self.nome_banco = nome_banco
        self.conn = sqlite3.connect(self.nome_banco)
        self.conn.execute
        self.cursor = self.conn.cursor()
        self.criar_tabela()
        
    def criar_tabela(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS contas (
                num_Conta INTEGER PRIMARY KEY,
                Nome_Usuario TEXT NOT NULL,
                saldo REAL NOT NULL
            )
        ''')
        self.conn.commit()
        
    def salvar_Conta(self, num_Conta, Nome_Usuario, saldo):
        self.cursor.execute('''
            INSERT INTO contas (num_Conta, Nome_Usuario, saldo)
            VALUES (?, ?, ?)
        ''', (num_Conta, Nome_Usuario, saldo))
        self.conn.commit()
        
    def atualizar_Conta(self, num_Conta, Nome):
        self.cursor.execute('''
            UPDATE contas SET Nome_Usuario = ? WHERE num_Conta = ?
        ''', (Nome, num_Conta))
        self.conn.commit()
          
    def fechar_conexao(self):
        self.conn.close()


class Conta_Bancaria:
    def __init__(self, nome_titular, numero_conta, saldo_inicial=0, banco_de_dados=None):
        self.nome_titular = nome_titular
        self.numero_conta = numero_conta
        self.saldo_inicial = saldo_inicial
        self.banco_de_dados = banco_de_dados
        self.salvar_conta()
        
    def atualizar_saldo(self, valor):
        self.banco_de_dados.atualizar_saldo(self.numero_conta, self.saldo)
        
    def salvar_conta(self):
        self.banco_de_dados.salvar_conta(self.numero_conta, self.nome_titular, self.saldo)
        
    def depositar_saldo(self, valor):
        if valor > 0:
            self.saldo += valor
            self.atualizar_saldo(valor)
            print(f"O valor de {valor} foi depositado com sucesso!")
        else: 
            print("Valor inválido!")
            
    def sacar(self,valor):
        if valor > 0:
            if self.saldo >= valor:
                self.saldo -= valor
                self.atualizar_saldo(valor)
                print(f"O valor de {valor} foi sacado com sucesso!")
            else: 
                print("Saldo insuficiente!")
        else: 
            print("Valor inválido!")
            
    def consultar_saldo(self):
        return self.saldo
    
    def transferir(self, valor, outra_Conta):
        if valor > 0:
            if self.saldo >= valor:
                self.saldo -= valor
                outra_Conta.saldo += valor
                self.atualizar_saldo(valor)
                outra_Conta.atualizar_saldo(valor)
                print(f"O valor de {valor} foi transferido com sucesso!")
            else: 
                print("Saldo insuficiente!")
        else: 
            print("Valor inválido!")

           
banco_de_dados = Banco_do_Jurandi()

conta1 = Banco_do_Jurandi("Joao", "12345", banco_de_dados=banco_de_dados)
conta2 = Banco_do_Jurandi("Maria", "54321", 1000, banco_de_dados=banco_de_dados)

print("Saldo inicial da conta de João:", conta1.consultar_saldo())
print("Saldo inicial da conta de Maria:", conta2.consultar_saldo())

conta1.depositar_saldo(1000)
conta1.sacar(200)
conta1.transferir(100, conta2)

print("Saldo atual da conta de João:", conta1.consultar_saldo())
print("Saldo atual da conta de Maria:", conta2.consultar_saldo())

banco_de_dados.fechar_conexao()
    
    

    