
"""
8.  Escreva um programa em Python que pede ao utilizador que lhe forneça uma sucessão de inteiros correspondentes
    a valores em segundos e que calcula o número de dias correspondentes a cada um desses inteiros. O programa
    termina quando o utilizador fornece um número negativo. O seu programa deve possibilitar a seguinte interação:
    Escreva um número de segundos? 45
    (um número negativo para terminar)
    O número de dias correspondente é 0.0005208333333333333
    Escreva um número de segundos? 6654441
    (um número negativo para terminar)
    O número de dias correspondente é 77.01899305555555
    Escreva um número de segundos? -1
    (um número negativo para terminar)
"""


def calculo(num1):
    total = num1 / 60 / 60 / 24

    return total

while __name__ == '__main__':
    continuar = 's'
    while continuar == 's':
        num1 = int(input('Insira os segundos: '))
        if num1 < 0:
            break
        else:
            print(f'{calculo(num1)}')
            continuar = input('Quer continuar? [s, n] ')
        print('Adeus!')