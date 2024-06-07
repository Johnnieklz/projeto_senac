# Realizamos a importação da biblioteca SQLite
'''import sqlite3 

# Abrimos a conexão e atributos ela a uma viriável
conexao = sqlite3.connect('exemplo.db')

#Utilizamos as opcões presentes na conexão
cursor = conexao.cursor()

# Executamos uma tarefa: criamos uma tabela caso ela não exista, especificamos os campos 
#que precisam ser preenchidos com nome do campo, tipo do campo e, caso precise,
# chave primária.
cursor.execute('''
   # CREATE TABLE IF NOT EXISTS usuarios (
  #              id INTEGER PRIMARY KEY AUTOINCREMENT,
   #         nome TEXT,
  #              idade INTEGER,
                
 #   cursor.execute("INSERT INTO usuarios (nome, idade) VALUES (?, ?)',('Alice' , 30)" )
  #  cursor.execute('INSERT INTO usuarios (nome, idade) VALUES (?, ?)',('Marcos' , 25))               
 #       )          
 #   ''')


#Comprometemos nossa alteração para o banco
#conexao.commit()

# Fechamos a conexão com o banco 
#conexao.close()
