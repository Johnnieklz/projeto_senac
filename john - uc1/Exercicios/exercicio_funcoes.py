# Calcular a os valores impares

'''def soma_impares(lista):
    impares = [num for num in lista if num % 2 != 0]
    return sum(impares)

numeros = input("Digite uma lista de números separados por espaço: ").split()
numeros = [int(num) for num in numeros]

soma = soma_impares(numeros)
print("A soma dos números impares da lista é: ", soma)
'''

# ==================================================================== #

#Calcular o máximo de números

'''
def maior_elemento(lista):
    return max(lista)

numeros1 = input("Digite uma lista de números separados por espaço: ").split()
numeros1 = [int(num) for num in numeros1]

maior = max(numeros1)

print("O maior número é: ", maior)
'''

# ==================================================================== #

# Calcular a média dos alunos 2.0

numAluno = int(input("Digite a quantidade de alunos: "))

media_alunos = []
notas_turma = []

for i in range(1, numAluno+1):
    print(f"Aluno {i}:")
    notas_aluno = []
    
    for j in range(1 , 4):
        nota = float(input(f"Insira a nota {j}: "))
        notas_aluno.append(nota)
        notas_turma.append(nota)
        
    media_alunos = sum(notas_aluno) / len(notas_aluno)
    notas_turma.append(media_alunos)
    print("A média do aluno é: " , media_alunos)
