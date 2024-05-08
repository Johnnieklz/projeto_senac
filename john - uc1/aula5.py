''' fatorial(a):
    if a == 0:
        return 1
    else:
        fat = 1
        for i in range(1, a+1):
            fat *= i 
        return fat 
    
x = int(input("Digite algum numero: "))

print("O fatorial de", x, "é:" , fatorial(x))
'''

"""
print = input("Digite seu nome: ")
print = int(input("Digite sua idade: "))
print = float(input("Digite sua altura: "))


tem_carro = input("Você possui carro? (Sim/Não) ")
tem_carro = tem_carro.lower() == "sim"
print ("Tem carro?" , "Sim" if tem_carro else "Não")
"""

"""
def contagem_regressiva():
    numero = int(input("Digite um número inteiro positivo: "))
    
    if numero <= 0:
        print("Por favor, digite um número inteiro positivo.")
        contagem_regressiva()
        
    else:
        while numero >= 0:
            print(numero)
            numero -=1 

contagem_regressiva()
"""

"""print (input("Digite um dos valores correspondentes: \n1 para Somar, \n2 para Subtração, \n3 para Multiplicação, \n4 para Divisão "))
    
   
soma = "1"
sub = "2"
mult = "3"
div = "4" 

def soma1(num1, num2):
    if soma == 1:
         return soma
    num1 = int(input("Digite um valor para a soma: " ))
    num2 = int(input("Digite um valor para a soma: " ))"""

def soma (a , b):
    return a + b
def subtracao (a , b):
    return a - b
def multiplicacao(a , b): 
    return a * b
def divisao (a , b):
    if a!= 0:
        return a / b
    else:
        return "Divisão inválida"
    
def calculadora():
    
    print("Bem-vindo a calculadora em Python!")
    print("Selecione a operação desejada: ")
    print("\n1: Adição \n2 Subtração \n3Multiplicação \n4Divisão")
    
    escolha = input("Digite sua escolha 1/2/3/4:" )
    if escolha in ('1' , '2' , '3' , '4'):
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        num3 = float(input("Digite o terceiro número: "))
        num4= float(input("Digite o quarto número: "))
        
        if escolha == '1':
            print("Resultado", soma(num1 , num2))
        elif escolha == '2':
            print("Resultado", subtracao(num1 , num2))
        elif escolha == '3':
            print("Resultado", multiplicacao(num1 , num2))
        elif escolha == '4':
            print("Resultado", divisao(num1 , num2))    
    else:
        print("Escolha inválida.")
        
calculadora()
        