'''     4. Escreva um programa que lê um número inteiro correspondente a um certo número de segundos e que escreve
        o número de dias, horas, minutos e segundos correspondentes a esse número. Por exemplo,
        Escreva o número de segundos? 345678
        dias: 4 horas: 0 mins: 1 segs: 18'''
'''
if __name__ == '__main__':
    def convertor(n):
        dia = n // (24 * 3600)

        n = n % (24 * 3600)
        horas = n // 3600

        n %= 3600
        minutos = n // 60

        n %= 60
        segundos = n

        print(f'Numero convertido é: {dia} dia/s, {horas} hora/s, {minutos} minuto/s, {segundos} segundos.')


    if __name__ == '__main__':
        continuar = 's' or 'S'
        while continuar == 's' or 'S':
            segundos = int(input(f'Insira o numero: '))
            print(f'Numero convertido é: {convertor(segundos)}')
            continuar = input('Quer continuar? [s, n] ')
        print('Adeus!')
'''
