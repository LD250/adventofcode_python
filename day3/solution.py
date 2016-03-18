def main():
    f = open('input.txt')
    content = f.read()
    start_pos = (0, 0)
    moves = {'^': (0, 1),
             '>': (1, 0),
             '<': (-1, 0),
             'v': (0, -1)}
    def next_pos(cur_pos, move):
        return tuple(cur_pos[i] + moves[move][i] for i in [0, 1])
    points = set([start_pos])
    for move in content:
        if move in moves:
            start_pos = next_pos(start_pos, move)
            points.add(start_pos)

    print(len(points))

    points = set([(0, 0)])
    santas_pos = [(0, 0), (0, 0)]
    for move_number, move in enumerate(filter(lambda m: m in moves, content)):
        santas_pos[move_number % 2] = next_pos(santas_pos[move_number % 2], move)
        points.add(santas_pos[move_number % 2])

    print(len(points))



if __name__ == "__main__":
    main()
