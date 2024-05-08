'''#Função
def operacoes (a , b):
    soma = a + b
    subtracao = a - b
    mult = a * b
    if b != 0: 
        div = a /b 
    else: 
        print("Divisão não permitida!")
        
    return soma, subtracao , mult , div 

num1 = 105
num2 = 44
resultado = operacoes(num1, num2)

print("Soma" , resultado[0] )
print("Subtração" , resultado[1] )
print("Multiplicação" , resultado[2] )
print("Divisão" , resultado[3] )
'''
      
'''     
#Fatorial de um número 
def fatorial(a):
    if a == 0:
        return 1
    else:
        fat = 1
        for i in range(1, a+1):
            fat *= i 
        return fat 
    
x = 10
print("O fatorial de", x, "é:" , fatorial(x))
'''
'''
a = input("Digite seu nome: ")
b = int(input("Digite algum número: "))
c = float(input("Digite seu ponto flutuante:"))

subtracao = c - b

def soma ( b, c):
    adicao = b + c 
    return adicao 

print("soma", adicao (b,c) )
''' 
