def main():
    f = open('input.txt')
    content = f.read()
    allowed_symbols = {'(': 1,
                       ')': -1}
    floor = sum([allowed_symbols.get(symb, 0) for symb in content]) 
    print floor
    floor = 0
    char = 1
    for symb in content:
        floor = floor + allowed_symbols.get(symb, 0)
        if floor == -1:
            print char
            break
        char += 1


if __name__ == "__main__":
    main()
