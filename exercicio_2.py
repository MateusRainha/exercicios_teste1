"""     2.  Escreva um programa em Python que lê valores correspondentes a uma
            distância percorrida (em Km) e o tempo necessário para a percorrer (em
            minutos), e calcula a velocidade média em:
            (a) Km / h
            (b) m/s             """

dist = int(input('Distância percorrida(km)= '))
tempo = int(input('Tempo necessário para percorrer x distância(min)= '))

print(f'Velocidade média(km/h)= {dist / (tempo / 60)} ')
print(f'Velocidade média(m/s)= {(dist * 1000) / (tempo * 60)} ')