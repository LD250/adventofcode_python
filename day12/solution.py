def main():
    f = open('input.txt')
    content = f.read()
    numbers = set([str(d) for d in range(10)])

    def calculate_total(content):
        number = ""
        minus_sign = False
        total = 0
        for symbol in content:
            if symbol in numbers:
                number += symbol
            elif symbol == '-' and not number:
                minus_sign = True
            elif number:
                if minus_sign:
                    total -= int(number)
                else:
                    total += int(number)
                number = ""
                minus_sign = False
        return total
    print calculate_total(content)

    # content = '[1,"red",5]{"d":"red","e":[1,2,3,4],"f":5}'

    def block_total(char_num):
        has_red = False
        inside_list = 0
        total = 0
        number = ""
        minus_sign = False
        while char_num < len(content):
            symb = content[char_num]
            if symb == '[':
                inside_list += 1
            elif symb == ']':
                inside_list -= 1
            if symb == ':' and 'red' == content[char_num + 2: char_num + 5]:
                has_red = True
            if symb == '{':
                inner_total = block_total(char_num + 1)
                total += inner_total[0]
                char_num = inner_total[1]
            elif symb in numbers:
                number += symb
            elif symb == '-' and not number:
                minus_sign = True
            elif number:
                if minus_sign:
                    total -= int(number)
                else:
                    total += int(number)
                number = ""
                minus_sign = False
                if symb == '}':
                    return (total if not has_red else 0, char_num)
            if symb == '}':
                return (total if not has_red else 0, char_num)
            char_num += 1
        return total
    print block_total(0)
if __name__ == "__main__":
    main()
