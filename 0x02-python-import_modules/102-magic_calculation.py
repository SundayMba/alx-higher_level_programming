#!/usr/bin/python3

if __name__ == '__main__':
    def magic_calcultion(a, b):
        add = __import__('magic_calculation').add
        sub = __import__('magic_calculation').sub

        if a < b:
            c = add(a, b)
            for i in range(4, 6):
                c = add(c, i)
            return c
        else:
            return sub(a, b)
