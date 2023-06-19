# Listas

# antes para ter 3 notas, aprendi a definir pedindo as três notas

nota1 = 7.9
nota2 = 9.7
nota3 = 8.2

#Com lista
notas = [7.9, 9.70, 8.2]


# Criando Listas
lista = [] #cria lista vazia
lista = list() # cria lista vazia  para converter alguma estrutura em uma lista

lista = [26, 'Pam', 3.14159, False] #permite diferentes tipos de variaveis
lista_de_listas = [10, [1, 2, 3]] # lista dentro de lista

#Indexação e Slices (fatiamento)
lista =[10, 'Pam', 3.1415, True]
print(lista[0]) # 0 é sempre a primeira posição de uma lista
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[-1]) # -1 é o último elemento e retorna o True da lista

# Slices

lista = [10, 50, 30, 40, 25, 60, 5]
print(lista[0:3]) #começa no indice 0 e vai até o indice 2 que são 10 (0), 50(1), 30(2)
print(lista[3:6]) #começa no pindice 0 e vai até o 3 que são 40, 25, 60 - não pega o índice 6 que é o 5 porque lista pega sempre 1 a menos
print(lista[3:]) #pega tudo do índice 3 em diante
print(lista[2:6:2]) # pega do índice 2 ao 6 de 2 em 2

# Interações com FOR

for elemento in lista: # percorre todos os elementos da lista
    print(elemento)
    # utilizando índices
    
    print('Cumprimento da lista: ', len(lista)) # Informe a quantidade de elementos em uma lista
    
for i in range(len(lista)):
    print(lista[i]) # acesso cada índice em cada interação, assim sairam todos os elementos da lista
# print(i) # assim imprime somente os 6 elementos porque o len da lista é 7"""