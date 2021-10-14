def funkcja(lista_a: list, lista_b: list):
    temp1 = [i for i in lista_a if i % 2 == 0]
    temp2 = [i for i in lista_b if not i % 2 == 0]
    return (temp1, temp2)

tt = [1,2,3,3,3,4]
t23=[3,4,6,7,8]
print(funkcja(tt, t23))