''' 7.  Escreva um programa em Python que lê o número de horas, que um empregado
        trabalhou numa dada semana e o seu salário/hora e calcula o ordenado semanal tendo em conta as horas extraordinárias.
        O salário é calculado do seguinte modo: se o número de horas fôr menor que 40 então salário é dado pelo produto
        do número de horas pelo salário hora, em caso contrário recebe horas extraordinárias as quais são pagas a dobrar.'''

if __name__ == '__main__':
    def salario(num1, num2):
        total = 0
        if num1 <= 40:
            salario = num1 * num2
            extra = 0
            total = salario + extra
        if num1 > 40:
            salario = (num1 * num2) - ((num1 - 40) * num2)
            extra = (num1 - 40) * (num2 * 2)
            total = salario + extra
        return total


    while __name__ == '__main__':
        continuar = 's'
        while continuar == 's':
            num1 = int(input('Insira as horas: '))
            num2 = int(input('Insira os preço/hora: '))
            print(f'O salário de {num1} horas é {salario(num1, num2)}')
            continuar = input('Quer continuar? [s, n] ')
        print('Adeus!')