# Metodos de listas - 

lista = [1, 3, 12, 8, 2]



# append
print(lista)
lista.append(3) # adiciona um elemento no final da lista

print('Depois do append: ',lista)


#Insert

lista.insert(2, 10) # adiciona um elemento em qualquer posição - nesse caso, adiciona no índice 2 o elemento 10
print("Depois do insert:", lista)

# extend
lista2 = [4, 2, 3] # juntar duas listas
lista.extend(lista2)
print("Depois do extend:", lista)


# pop

lista.pop() # remove elementos - se não especificar, remove o ultimo elemento
print("Lista após o pop:", lista)

lista.pop(0) #elimina o elemento no índice especificado, no caso 0
print("Lista após o pop:", lista)

# remove
lista.remove(3) # você informa qual elemento quer tirar da lista (sempre o primeiro elemento caso tenha mais de um)
print("Depois do remove", lista)

# count

print("Quantidade de 2 na lista:", lista.count(2)) #mostra quantas vezes um determinado elemento aparece em uma lista

#indez

print("Índice do elemento 12:", lista.index(12))

#sort

lista.sort() #ordena de forma crescente
print(lista)

lista.sort(reverse = True) # ordena de forma invertida
print(lista)

# funções para lista

#len
print(len(lista)) # informa quantos elementos tem em uma lista

# sum

print(sum(lista)) # soma todos os elementos de uma lista

# max

print("Maior elemento da lista", max(lista))

# min

print("Menor elemento da lista:", min(lista))