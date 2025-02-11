lista_mea = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

print(f'Lista initiala: {lista_mea}')

lista_mea.sort()

print(f'Lista sortata ascendent: {lista_mea}')

lista_mea.sort(reverse=True)

print(f'Lista sortata descendent: {lista_mea}')

# afisam elementele pare din lista
elemente_pare = []
lista_mea.sort()
for z in lista_mea:
    if z % 2 == 0:
        elemente_pare.append(z)
print(f'Elemente pare din lista: {elemente_pare}')

# afisam elementele impare din lista
elemente_impare = []
for z in lista_mea:
    lista_mea.sort()
    if z % 2 != 0:
        elemente_impare.append(z)
print(f'Elemente impare din lista: {elemente_impare}')

lista_mea.sort()

print(f'Lista mea ordonata {lista_mea}')

print(f'Elemente pare din lista ordonata: {lista_mea[1::2]}')

print(f'Elemente impare din lista ordonata {lista_mea[0::2]}')


