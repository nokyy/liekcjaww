class FileManager:

    def __init__(self, file_name) -> None:
        self.file_name = file_name
    
    def read_file(self):
        with open(self.file_name, 'r') as file:
            lines = file.readlines()
        return lines

    def update_file(self, text_data):
        with open(self.file_name, 'a') as file:
            file.write(text_data)
        