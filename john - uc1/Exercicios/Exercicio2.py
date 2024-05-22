
# ==================================================================== #

#                       Classificação de Idade

# ==================================================================== #
'''
crianca = adolescente = adulto = idoso = 0

for n in range(5):
    idade = int(input("Digite a sua idade:"))

    
    if idade < 13:
        crianca = crianca + 1
    elif 13 <= idade < 18:
        adolescente = adolescente + 1
    elif 18 <= idade < 60:
        adulto = adulto + 1
    else:
        idoso = idoso + 1

print("crianças: ", crianca)
print("adolescentes: ", adolescente)
print("Pessoas adultas: ", adulto)
print("Idosos: ", idoso)
'''

# ==================================================================== #

#                 Calculadora de Fatorial (Questão: 6)

# ==================================================================== #
'''
import math

print("Calculadora de fatorial! \nInstruções: \n 1 - Digite o valor desejado \n 2 - Espere o resultado")
a = int(input("Digite o valor desejado: "))

fatorial = math.factorial(a)
print(f"Fatorial de {a} é de {fatorial}")

'''
# ==================================================================== #


# ==================================================================== #

#                 Contagem de Frequência de Caracteres

# ==================================================================== #
'''
from collections import Counter

carac = str(input("Digite alguma frase ou palavra: "))
caracList = carac.split()
contador = Counter(carac)
print(contador)
'''
# ==================================================================== #   
    
#                       Cadastro de Contatos    
    
# ==================================================================== #
'''
# Passo 1: Criar uma lista vazia para armazenar os contatos
contatos = []

# Passo 2: Definir a função para adicionar um novo contato
def adicionar_contato():
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    email = input("Digite o email do contato: ")
    novo_contato = {"Nome": nome, "Telefone": telefone, "Email": email}
    contatos.append(novo_contato)
    print("Contato adicionado com sucesso!")

# Passo 3: Definir a função para exibir todos os contatos
def exibir_contatos():
    if len(contatos) == 0:
        print("Não há contatos cadastrados.")
    else:
        print("Lista de contatos:")
        for contato in contatos:
            print("Nome:", contato["Nome"])
            print("Telefone:", contato["Telefone"])
            print("Email:", contato["Email"])
            print("------------------------")

          
# Passo 4: Criar o loop principal do programa
while True:
    print("\nEscolha uma opção:")
    print("1. Adicionar novo contato")
    print("2. Exibir contatos")
    print("3. Sair")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        adicionar_contato()
    elif opcao == "2":
        exibir_contatos()
    elif opcao == "3":
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
'''
# ==================================================================== #   
    
#                      Gerador de Senha (Questão: 7)
    
# ==================================================================== #
'''
import re

def validar_senha(senha):
    if (len(senha) >= 8 and 
        re.search(r"[A-Z]", senha) and 
        re.search(r"[a-z]", senha) and
        re.search(r'\d', senha) and
        re.sarch(r"[!@#$%¨&*()_-+/*?:;.,><{}]")):
        return True
    else:
        return False
print("Sua senha é: ", validar_senha)
'''
# ==================================================================== #   
    
#                      Lista de Compras (Questão: 5)
    
# ==================================================================== #

def lista_de_compras():
    compras = []
    while True:
        print("Menu da Lista de Compras! \n 1. Adicionar Item \n2. Remover Item \n3. Visualizar Item \n4. Sair")
        escolha = input("Digite o número da opção desejada: ")
        
        if escolha =="1":
            item = input("Digite o item que deva ser adicionado")
            compras.append(item)
        elif escolha =="2":
            item = input("Digite o item que quer remover")
            if item in compras:
                compras.remove(item)
            else: 
                print("Item não encontrado!")
                
        elif escolha =="3":
            print("Itens da Lista de Compras até Agora: ")
            for item in compras:
                print(item)
        elif escolha == "4":
            print("Saindo...")
            break
    
        else: 
            print("Opção Inválida. Tente novamente!")
lista_de_compras()


