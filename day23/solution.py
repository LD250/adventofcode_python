def main():
    f = open('../input.txt')
    content = f.read()
    lines = content.strip().replace(',', '').split('\n')

    operations = [line.split(' ') for line in lines]
    for operation in operations:
        if operation[0] in ['jio', 'jie']:
            operation[2] = int(operation[2])
        elif operation[0] == 'jmp':
            operation[1] = int(operation[1])
    def run_program(registers):
        i = 0
        while i < len(operations):
            plus = 1
            op = operations[i]
            instr = op[0]
            if instr == 'hlf':
                registers[op[1]] /= 2
            elif instr == 'tpl':
                registers[op[1]] *= 3
            elif instr == 'inc':
                registers[op[1]] += 1
            elif instr == 'jmp':
                plus = op[1]
            elif instr == 'jie':
                if registers[op[1]] % 2 == 0:
                    plus = op[2]
            elif instr == 'jio':
                if registers[op[1]] == 1:
                    plus = op[2]

            i += plus

        return registers

    print run_program({'a': 0, 'b': 0})
    print run_program({'a': 1, 'b': 0})

if __name__ == "__main__":
    main()
