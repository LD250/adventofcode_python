from functools import partial


def main():
    f = open('../input.txt')
    lines = f.readlines()
    actions = {'turn on': lambda light_status: 1,
               'turn off': lambda light_status: 0,
               'toggle': lambda light_status: 0 if light_status else 1}

    def read_instruction(lights, actions):
        for line in lines:
            action, from_coordinates, _, to_coordinates = line.rsplit(' ', 3)
            from_coordinates = from_coordinates.split(",")
            to_coordinates = to_coordinates.split(",")
            for x in xrange(int(from_coordinates[0]), int(to_coordinates[0]) + 1):
                for y in xrange(int(from_coordinates[1]), int(to_coordinates[1]) + 1):
                    lights[x][y] = actions[action](lights[x][y])
        return sum(map(sum, lights))

    lights = [[0] * 1000 for x in xrange(1000)]
    print(read_instruction(lights, actions))

    actions = {'turn on': lambda light_status: light_status + 1,
               'turn off': lambda light_status: light_status - 1 if light_status > 0 else 0,
               'toggle': lambda light_status: light_status + 2}
    lights = [[0] * 1000 for x in xrange(1000)]
    print(read_instruction(lights, actions))

if __name__ == "__main__":
    main()
