# tablero
# variables para cada casilla del 1-9 
#Cada variable puede estar en no de tres estados. Disponible, jugada por el humano, jugada por la maquina 
#Representados por los valores. 0, 1 y 2 repectivamente

c1 = 0
c2 = 0
c3 = 0
c4 = 0
c5 = 0
c6 = 0
c7 = 0
c8 = 0
c9 = 0

# Valores que representan victoria de la maquina o el humano

diah = c1 + c5 + c9 == 3 or c3 + c5 + c7 == 3
diam = c1 + c5 + c9 == 6 or c3 + c5 + c7 == 6
