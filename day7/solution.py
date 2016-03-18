
def main():
    f = open('input.txt')
    lines = f.read()
    lines = lines.split('\n')
    parsed_code = {}
    init_vars = {}
    for line in lines:
        if line:
            left, right = line.split('->')
            operations = left.strip().split(' ')
            right = right.strip()
            if len(operations) == 1:
                if operations[0].isdigit():
                    init_vars[right] = int(operations[0])
                else:
                    parsed_code[right] = {'vars': [operations[0]],
                                        'op': 'INT'}
            elif len(operations) == 2:
                parsed_code[right] = {'vars': [operations[1]],
                                    'op': operations[0]}
            else:
                parsed_code[right] = {'vars': [operations[0], operations[2]],
                                    'op': operations[1]}

    def find_a(init_vars, parsed_code):
        if 'a' in init_vars:
            return init_vars['a']
        else:
            new_init = dict(init_vars)
            new_parsed = {}
            for wire, expression in parsed_code.iteritems():
                new_vars = []
                check_var_value = False
                for var in expression['vars']:
                    if var in init_vars:
                        new_vars.append(init_vars[var])
                        check_var_value = True
                    else:
                        new_vars.append(var)
                op = expression['op']
                new_parsed[wire] = {'vars': new_vars,
                                    'op': op}
                if check_var_value:
                    #new_parsed['vars'] = 
                    inited_var = None
                    try:
                        new_vars = [int(v) for v in new_vars]
                        if op == 'AND':
                            inited_var = new_vars[0] & new_vars[1]
                        elif op == 'OR':
                            inited_var = new_vars[0] | new_vars[1]
                        elif op == 'NOT':
                            inited_var = ~new_vars[0]
                        elif op == 'INT':
                            inited_var = int(new_vars[0])
                        elif op == 'LSHIFT':
                            inited_var = new_vars[0] << new_vars[1]
                        elif op == 'RSHIFT':
                            inited_var = new_vars[0] >> new_vars[1]
                    except Exception as e:
                        pass
                    if inited_var is not None:
                        new_init[wire] = inited_var
                        del new_parsed[wire]
            return find_a(new_init, new_parsed)

    a_wire = find_a(init_vars, parsed_code)
    print a_wire
    init_vars['b'] = a_wire
    new_a_wire = find_a(init_vars, parsed_code)
    print new_a_wire

if __name__ == "__main__":
    main()
