jeden = (123123, 'jan owalny')
dwa = (2323, 'kot orbitalny')

lista = list(jeden+dwa)
print(f'{lista}')


slownik_ejden ={"numer_indeksu":jeden[0], "imie_nazwisko":jeden[1], "wiek":123, "email":'awoo', 'rok':1992, "address":"awoo2"}
slownik_dwa ={"numer_indeksu":dwa[0], "imie_nazwisko":dwa[1], "wiek":1223, "email":'awosso', 'rok':19922, "address":"awsdoo2"}
print(slownik_ejden)
print(slownik_dwa)