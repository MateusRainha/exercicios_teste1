'''14. Escreva um programa que lê um inteiro e calcula a soma dos seus dígitos.'''

def digito(valor):
    # Contar o número de digitos
    #digitos = len(str(valor))

    # Soma de seus digitos
    valor = str(valor)
    digitos = 0
    for x in range(len(valor)):
        digitos += int(valor[x])

    return digitos


if __name__ == '__main__':
    while True:
        try:
            num = int(input('Qual é o número? '))

            print(f'A soma dos dígitos do número {num} é {digito(num)}.')

            continuar = input('Repetir (s | n)? ')
            if continuar == 'n':
                break

        except ValueError:
            print('Digite um valor válido')

    print(f'Adeus!')