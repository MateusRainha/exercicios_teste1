"""     2. Escreva um programa em Python que lê valores correspondentes a uma
        distância percorrida (em Km) e o tempo necessário para a percorrer (em
        minutos), e calcula a velocidade média em:
        (a) Km / h
        (b) m/s             """

dist = int(input('Distancia(km)= '))
tempo = int(input('tempo(min)= '))

print(f'{dist / (tempo / 60)} km/h')
print(f'{(dist * 1000) / (tempo * 60)} m/s ')