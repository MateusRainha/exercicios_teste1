'''     4.  Escreva um programa que lê um número inteiro correspondente a um certo número de segundos e que escreve
            o número de dias, horas, minutos e segundos correspondentes a esse número. Por exemplo,
            Escreva o número de segundos? 345678
            dias: 4 horas: 0 mins: 1 segs: 18'''

#https://acervolima.com/programa-python-para-converter-segundos-em-horas-minutos-e-segundos/

if __name__ == '__main__':
    def dia(valor):
        dias = valor / 60
        dias = dias / 60
        dias = dias / 24

        return dias


    def hour(valor):
        hours = valor % (24 * 3600)
        hours = hours // 3600

        return hours


    def min(valor):
        mins = valor % (24 * 60)
        mins = mins // 60

        return mins


    def seg(valor):
        segs = valor
        segs %= 60

        return segs


    if __name__ == '__main__':
        while True:
            try:
                segundos = int(input('Quantos segundos? '))

                print(f'dias: {int(dia(segundos))} hours: {int(hour(segundos))} mins: {int(min(segundos))} segs: {int(seg(segundos))}')

                continuar = input('Repetir (s | n)? ')
                if continuar == 'n':
                    break

            except ValueError:
                print('Digite um valor válido')

        print(f'Adeus!')