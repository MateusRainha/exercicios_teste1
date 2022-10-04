'''16. Escreva um programa que lê um número e cria uma capicua cuja primeira metade é o número lido. Por exemplo:
       Escreva um número-> 347
       347743'''

num = input('Escreva um número: ')
print(f'A capicua do número {num} é {num}{num[::-1]}')