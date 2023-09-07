def manual_input():
    query = input("What?\n")
    with open("temp_file", 'r+') as file:
        file.write(query)
        file.seek(0)
        exec(file.readline())
        file.truncate(0)
