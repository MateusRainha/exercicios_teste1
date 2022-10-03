'''     3. Escreva um programa em Python que pede ao utilizador que lhe forneça um inteiro correspondente a um número de segundos e
        que calcula o número de dias correspondentes a esse número de segundos. O seu programa deve permitir a interação:
        Escreva um número de segundos? 65432998
        O número de dias correspondentes é 757.3263657407407'''

if __name__ == '__main__':
    nsegundos = int(input('Escreva um número de segundos: '))
    print(f'O número de dias correspondentes é {nsegundos / 86400}')
