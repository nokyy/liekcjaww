lista = [ x for x in range(1,11,1) ]
lista2 = lista[5::]

for i in lista:
    lista.pop()

print(f'{lista}\n{lista2}')

lista = lista + lista2
lista.reverse()
lista.append(0)
lista.reverse()
lista3 = lista.copy()
print(lista)
print(lista3[::-1])