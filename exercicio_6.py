'''     6.  Escreva um programa em Python que lê três números e que diz qual o
            maior dos números lidos.        '''

numeros = []
numeros.append(int(input(f'1º número: ')))
numeros.append(int(input(f'2º número: ')))
numeros.append(int(input(f'3º número: ')))
print(numeros)

menor = numeros[0]
maior = numeros[0]
for x in range(1, len(numeros)):
    if numeros[x] < menor:
        menor = numeros[x]
    if numeros [x] > maior:
        maior = numeros[x]
print(f'O maior é {maior}')
print(f'O menor é {menor}')