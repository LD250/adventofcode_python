def main():
    f = open('input.txt')
    content = f.read()
    lines = [line for line in content.split('\n') if line]
    total_difference = 0
    def line_diff(line):
        code_len = len(line)
        mem_len = 0
        i = 1
        while i < code_len - 1:
            if line[i] == '\\':
                if line[i + 1] == 'x':
                    i += 4
                else:
                    i += 2
            else:
                i += 1
            mem_len += 1
        return code_len - mem_len

    print(sum(map(line_diff, lines)))
    def line_diff2(line):
        code_len = len(line)
        encoded_len = reduce(lambda l, c: l + (2 if c in ['"', '\\'] else 1), line, 2)
        return encoded_len - code_len
    print(sum(map(line_diff2, lines)))


if __name__ == "__main__":
    main()
