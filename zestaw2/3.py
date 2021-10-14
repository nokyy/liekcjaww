def funkcja(text, letter):
    return "".join(i for i in text if i not in letter)

print(funkcja('awooo', 'o'))