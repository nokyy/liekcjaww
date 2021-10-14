from file_manager import FileManager

test = FileManager('C:/Users/Tyranozaur/Desktop/AAAAA/cwwww/zestaw2/test.txt')
print(test.read_file())
test.update_file('penis`123')
print(test.read_file())
test.update_file('\npenis`123')
print(test.read_file())
