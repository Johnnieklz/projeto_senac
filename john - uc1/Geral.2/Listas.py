'''#Adiciona valores ao final da lista 

a = []
a = [1 , 2 , 3]
a.append (4)


#Inserir itens pela posição (n1 = posição , n2 = valor)

a.insert(1 , 5)
print(a)


#Remove o item pela posição

a.remove(5)
print(a)


# Remove o último item da lista

ultimo_elemento = a.pop()
print(ultimo_elemento)
print(a)


#Deleta um item selecionado pela posição

del a[0]
print(a)   

'''

x = [1, 2, 3, 4, 5]

a = int(input("Digite um número: "))
x.append(a)

b = str(input("Digite alguma palavra: ")) 
x.insert(0 , b)

print("O valor da lista é:", x)
