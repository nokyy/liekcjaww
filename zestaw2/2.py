def funkcja(data_text: dict):
    length = str(data_text).__len__()
    letters = [i for i in str(data_text)]
    big_letters = str(data_text).upper()
    small_letters = str(data_text).lower()

    return(length, letters[::], big_letters, small_letters)

test = {
    'awoo':'awoOOOo',
    'aff':'aFFFf',
}
print(funkcja(test))