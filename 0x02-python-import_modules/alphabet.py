def print_alphabet(letter = 65):
    if letter <= 90:
        print("{}".format(chr(letter)), end='')
        print_alphabet(letter + 1)
print_alphabet()
