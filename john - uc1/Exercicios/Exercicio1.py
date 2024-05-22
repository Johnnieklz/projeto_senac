'''number = int(input('Numero: '))
ePrimo = 0

for i in range(1, (number + 1)):        
  if number % i == 0:
    ePrimo += 1
    
if ePrimo  == 2 :
  print('primo')
else:
  print('nao primo')


ano = int(input("Digite o ano: "))

if (ano%4==0 and ano%100!=0) or (ano%400==0):
    print("O ano é bissexto!")
else:
    print("Não é bissexto!")



c= float(input("Digite a temperatura em Celsius: "))
f = 32 + (9/5)*c
print("A temperatura em Celsius é", c, "°C")
print("A temperatura em Fahrenheit é", f, "°F")


a = int(input("Digite algum número: "))
b = int(input("Digite algum número: "))
c = int(input("Digite algum número: "))
d = int(input("Digite algum número: "))
e = int(input("Digite algum número: "))

f = a + b + c + d + e  
g = f /5
print("O valor é:  ", g) 



a = float(input("Digite o primeiro lado: "))
b = float(input("Digite o segundo lado: "))
c = float(input("Digite o terceiro lado: "))
 
if (a + b < c) or (a + c < b) or (b + c < c): 
     print("não é um triangulo ")
     
elif (a == b) and (a == c):
        print("É um triangulo equilatero ")

elif (a == b) and (a == c) and (b == c): 
    print("É um triangulo isoceles")
    
else: 
    print("Escaleno ")

'''

    

  
'''
def conta_vogais(word):
    vogais = 'aeiouAEIOU'
    count = 0
    for char in word:
      if char in vogais:
        count += 1
    return count
  
word = input("Digite uma palavra: ")
contador_geral = conta_vogais(word)
print("A palavra", word, "contém", contador_geral, "vogais")
'''
    

'''
from random import choice
import string

tamanho_da_senha = int(input("Quantos dígitos você quer na sua senha? "))
caracteres = string.ascii_letters + string.digits + string.punctuation
senha_segura = ''
for i in range(tamanho_da_senha):
  senha_segura += choice(caracteres)

print("A senha (segura) gerada é: ",senha_segura)
'''
'''
def palindromo(word):
  word = word.lower()
  return word == word[::-1]

word = input("Digite uma palvra que deverá ser analisada se é um palindromo: ")
if palindromo(word):
  print("A palavra é palindromo!")
else: 
  print("A palavra não é  um palindromo")
'''