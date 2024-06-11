import sqlite3

class ItemEstoque:
    def __init__(self, nome, marca, modelo, preco, quantidade):
        self.nome = nome
        self.marca = marca
        self.modelo = modelo
        self.preco = preco
        self.quantidade = quantidade

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}\nMarca: {self.marca}\nModelo: {self.modelo}\nPreço: R$ {self.preco}\nQuantidade: {self.quantidade}")

class Estoque:
    def __init__(self, db_name="estoque.db"):
        self.conn = sqlite3.connect(db_name)
        self.criar_tabela()

    def criar_tabela(self):
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS itens (
                    id INTEGER PRIMARY KEY,
                    nome TEXT NOT NULL,
                    marca TEXT NOT NULL,
                    modelo TEXT NOT NULL,
                    preco REAL NOT NULL,
                    quantidade INTEGER NOT NULL
                )
            """)

    def inserir_item(self, item):
        with self.conn:
            self.conn.execute("""
                INSERT INTO itens (nome, marca, modelo, preco, quantidade)
                VALUES (?,?,?,?,?)""", (item.nome, item.marca, item.modelo, item.preco, item.quantidade))
        print("Item adicionado ao estoque com sucesso!")

    def remover_item(self, nome_item):
        with self.conn:
            cursor = self.conn.execute("DELETE FROM itens WHERE nome =?", (nome_item,))
        if cursor.rowcount > 0:
            print("Item removido do estoque com sucesso!") 
        else: 
            print("Item não encontrado!")

    def editar_item(self, nome_item, nova_quantidade):
        with self.conn:
            cursor = self.conn.execute("UPDATE itens SET quantidade = ? WHERE nome = ?", (nova_quantidade, nome_item))
            if cursor.rowcount > 0:
                print(f"Quantidade do item {nome_item} atualizada com sucesso!")
            else:
                print(f"Item {nome_item} não encontrado!")

    def exibir_itens(self):
        with self.conn:
            cursor = self.conn.execute("SELECT * FROM itens")
            for linha in cursor:
                print(f"Nome: {linha[1]}\nMarca: {linha[2]}\nModelo: {linha[3]}\nPreço: R$ {linha[4]}\nQuantidade: {linha[5]}")

    def calcular_valor_total(self):
        with self.conn:
            cursor = self.conn.execute("SELECT SUM(preco * quantidade) FROM itens")
            total = cursor.fetchone()[0]
            print(f"Valor total do estoque: {total}")

    def interface(self):
        while True:
            print("\nEscolha uma opção:")
            print("\n1. Adicionar item.")
            print("\n2. Remover item.")
            print("\n3. Editar quantidade de um item.")
            print("\n4. Exibir itens.")
            print("\n5. Calcular valor total do estoque.")
            print("\n6. Sair.")

            opcao = input("\nDigite o número da opção desejada: ")

            if opcao == "1":
                nome = input("Nome do item: ")
                marca = input("Marca do item: ")
                modelo = input("Modelo do item: ")
                preco = float(input("Preço do item: "))
                quantidade = int(input("Quantidade do item: "))
                item = ItemEstoque(nome, marca, modelo, preco, quantidade)
                self.inserir_item(item)

            elif opcao == "2":
                nome_item = input("Digite o nome do item que será excluído: ")
                self.remover_item(nome_item)
            elif opcao == "3":
                nome_item = input("Digite o nome do item que terá a quantidade editada: ")
                nova_quantidade = int(input("Digite a nova quantidade: "))
                self.editar_item(nome_item, nova_quantidade)
            elif opcao == "4":
                self.exibir_itens()
            elif opcao == "5":
                self.calcular_valor_total()
            elif opcao == "6":
                print("Encerrando programa...")
                break
            else:  
                print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    estoque = Estoque()
    estoque.interface()
