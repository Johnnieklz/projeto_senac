import random


def numAleatorio():
    numero_aleatorio = random.randint(1 , 100)
    tentativas = 0
    
    while True:
        usuario = int(input("Digite algum palpite e verá se está correto ou não: "))
        #tentativa += 1 
        
        if usuario < numero_aleatorio:
         print("Digite outro valor maior!")
        
        elif usuario > numero_aleatorio:
         print("Digite outro valor maior!")
     
        else:
            print(f"Voçê acertou o número {numero_aleatorio}")
        break
      
numAleatorio()
