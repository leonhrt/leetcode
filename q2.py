players = [
    [9, 5, 11],  # Jugador 1
    [4, 12, 3],  # Jugador 2
    [2, 10, 13]   # Jugador 3
]

# Ordenamos los ataques de cada jugador
for i in range(3):
    players[i].sort()

# Ahora comparamos si un jugador puede ganar a otro
winners = set()

for i in range(3):
    for j in range(3):
        if i != j and all(players[i][k] >= players[j][k] for k in range(3)):
            winners.add(i)

print(len(winners))  # Esto te dice cuántos jugadores pueden ganar
