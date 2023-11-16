class ManualInput:
    @staticmethod
    def manual_input():
        query = input("What?\n")
        with open("../resources/temp_file", 'r+') as file:
            file.write(query)
            file.seek(0)
            exec(f'print({file.readline()})')
            file.truncate(0)
