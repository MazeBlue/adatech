numero_sorteado = 15

numero_escolhido = int(input("Informe um numero entre 1 e 20: "))

while numero_escolhido != numero_sorteado:
    print('Você errou! Tente novamente...')
print("Parabens! Você acertou.")

# exemplo 02: Estrutura com contador

contador = 0
while contador < 3:
    print(contador)

    contador = contador +1



"""if numero_sorteado == numero_escolhido:
    print("VOcê acertous!")
else:
    print("Você errou!")"""