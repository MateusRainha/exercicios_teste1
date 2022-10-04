"""
9.  Escreva um programa em Python que lê uma sequência de dígitos, sendo
    cada um dos dígitos fornecido numa linha separada, e calcula o número
    inteiro composto por esses dígitos, pela ordem fornecida. Para terminar a
    sequência de dígitos é fornecido ao programa o inteiro
    O seu programa deve permitir a interação:
    Escreva um dígito? 3
    (-1 para terminar)
    Escreva um dígito? 2
    (-1 para terminar)
    Escreva um dígito? 5
    (-1 para terminar)
    Escreva um dígito? 7
    (-1 para terminar)
    Escreva um dígito? -1
    (-1 para terminar)
    O número é: 3257
    """
def divisao(numero):
    total = 0
    for n in range(1, numero + 1):
        total = numero / n
        total = total + 1

    return total


if __name__ == '__main__':
    continuar = 's' or 'S'
    while continuar == 's' or 'S':
        numeros = []
        while True:
            n = int(input('Numero: '))
            if n != -1:
                numeros.append(n)
            if n == -1:
                break

        numeros = ''.join(str(x) for x in numeros)

        numeros_int = int(numeros)
        print(f'O número é: {numeros_int}')

        divisores = divisao(numeros_int)
        if divisores >= 2:
            print(f'O numero {numeros_int} é um número composto')
        else:
            print(f'O numero {numeros_int} não é composto.')


        continuar = input('Quer continuar? [s, n]')
        if continuar == 'n':
            break