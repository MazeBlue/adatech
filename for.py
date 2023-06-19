"""for variavel in range(6): # aqui ele irá imprimir variaveis de 0 à 5, pois o contador sempre começa no 0 quando não definido
    print(variavel)
"""

"""for variavel in range(1, 11): # aqui definimos o inicio da variavel em 1 até 10
    print(variavel)"""

"""for variavel in range(1, 12, 3): # aqui defino para iniciar do 1 e ir até o 11 pulando de 3 em 3
    print(variavel)"""


soma = 0

for i in range(1,4): # se defino o contador em 3, ele vai pedir 3 notas, mas começando do 0, para pedir 1,2,3 defino o contador de 1,4
    nota = float(input(f"Informe sua nota {i}: ")) # f'string - f na frente da string pra injetar a variavel dentro das chaves
    soma = soma + nota
print(f"A soma das notas é: {soma}")

media = soma/3
print(f"A média das notas é: {media}")