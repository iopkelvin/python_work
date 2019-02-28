filename = "guest_book.txt"

with open(filename, 'w') as file_object:
    names = True
    while names:
        name = input("Please enter your name:")
        file_object.write(name + '\n')
        if len(name) > 0:
            print("Hello, ", name)
            names = True
        else:
            names = False
