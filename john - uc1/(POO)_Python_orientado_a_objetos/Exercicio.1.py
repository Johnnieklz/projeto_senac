'''class Pessoa(object):
    def __init__(self, nome, idade, peso, altura ):
        self.nome = nome
        self.idade = idade
        self.peso = peso 
        self.altura = altura
        
    def Envelhecer(self):
        
        self.idade = self.idade + 1
        print(f"Sua idade está: {self.idade}")
        
        if self.idade <= 21:
            self.altura = self.altura + 0.5
            print(f"Sua altura está: {self.altura}")
            
        else:
            print("Você está mais velho")
    
    def Engordar (self):
        self.peso = self.peso + 1
        print(f"Seu peso está: {self.peso} kg")       
            
    

pessoas = Pessoa("John", 18, 70, 1.70)

print("Nome: %s" % pessoas.nome )
print("Idade: %s" % pessoas.idade)
print(f"Peso igual {pessoas.peso} kg")
print("Altura: %s" % pessoas.altura)

'''

# ==================================================================== #   
    
#                            Correção
    
# ==================================================================== #

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        
    def Envelhecer(self):
        self.idade += 1
        if self.idade <= 21:
            self.Crescer (0.5)
        
    def Engordar(self, peso):
        self.peso += peso
        
    def Emagrecere(self, peso):
        self.peso -= peso
        
    def Crescer(self, altura):
        self.altura += altura
        
    def __str__(self):
        return f"Nome: {self.nome}\nIdade: {self.idade}\nPeso: {self.peso}\nAltura: {self.altura}"
        
pessoas = Pessoa("John", 18, 100, 1.80)
print("Dados iniciais")
print("pessoas")

pessoas.Envelhecer()
pessoas.Engordar(10)

print("Dados após envelhecer e engordar")
print(pessoas)
        

            













