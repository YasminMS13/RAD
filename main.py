# arquivo = open("texto.txt", "r") # Abre o arquivo "texto.txt"

# print(arquivo.readline()) # Ler uma linha 
# print(arquivo.readline()) # Ler outra linha
# print(arquivo.seek(0)) # Coloca o cursor na posicao 0 do arquivo
# print(arquivo.readlines()) # Ler todas as linhas, junto com as quebras (\n)
# print(arquivo.seek(0)) 

# print(arquivo.read()) # ler o arquivo todo
# print(arquivo.tell()) # Retorna a quantidade de caracteres

# arquivo.close() # Fecha o arquivo
# print(arquivo.closed)

# print(arquivo.read())
# print(arquivo.seek(0))
# print(arqivo.read(8))

# print(arquivo.name)
# print(arquivo.mode)
# print(arquivo.mode)
# print(arquivo.closed)

# arquivo = open("novo.txt", "w") # Cria um novo arquivo, se nao existir

# arquivo.write("Arquivo de escrita") # Escreve no arquivo

# arquivo.close() # Fecha o arquivo
# print(arquivo.closed) # Retorna se o arquivo ta fechado ou nao ( True ou False )

# arquivo = open("frutas.txt", "w")
# arquivo.write("Banana" + "\n")
# arquivo.write("Uva" + "\n")
# arquivo.write("Mamao" + "\n")

# arquivo.close()

# precos = [20, 100, 500, 600]

# with open("precos roupas.txt", "w") as arquivo: # Cria um arquivo e ao sair do with, fecha automaticamente o arquivo
#     for preco in precos:
#         arquivo.write(str(preco) + "\n")

# print(arquivo.closed)

# precos = [800]

# with open("precos roupas.txt", "a") as arquivo:
#     for preco in precos:
#         arquivo.write(str(preco) + "\n")
# diciplinas = ["RAD \n", "introducao a c \n", "programacao 1 \n"]
# with open("diciplinas.txt", "w") as file:
#     file.write("relacao de diciplinas \n")
#     file.writelines(diciplinas)
# with open("diciplinas.txt", "r")as file:
#     print(file.read())
# with open("texto.txt", "r") as arquivo:
#     print("representacao original da linha")
#     for linha in arquivo:
#         print(repr(linha))
# with open("texto.txt", "r")as arquivo:
#     print("conteudo da linha")
#     for linha in arquivo:
#         linha_=linha.strip()
#     print(repr(linha_))
# minha_lista = ["arroz", "feijao", "carne"]
# lista_=','. join(minha_lista)
# with open("texto_.txt", "w")as arquivo:
#     arquivo.write(lista_)
import os

try:
    os.remove("teste.txt")
    print("arquivo foi removido")
except FileNotFoundError as erro:
    print("arquivo inexistente")
    print("descricao", erro) 