# Dicionários

#Criando Dicionarios

dicionario = {} # chama dicionario e abre chaves {} - definindo um diicionario vazio
dicionario = dict() # - cria um dicionario vazio

dicionario = {' nome': 'Pam', 'idade': 28, 'altura': 1.58} # criando dicionario com conteúdo

print(dicionario)
print(dicionario['idade'])

# Adicionando elementos a um dicionario

dicionario['programador'] = True

print(dicionario)


# Iterando sobre um dicionário

for chave in dicionario:
    print(chave, dicionario[chave])

#testando a existencia de uma chave

print('peso' in dicionario)
print('altura' in dicionario)