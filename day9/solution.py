from collections import defaultdict

def main():
    f = open('input.txt')
    content = f.read()
    lines = [line for line in content.split('\n') if line]
    connections = defaultdict(list)
    for line in lines:
        connection, distance = line.split(' = ')
        distance = int(distance)
        city_from, city_to = connection.split(' to ')
        connections[city_from].append((city_to, distance))
        connections[city_to].append((city_from, distance))

    def get_all_routes(city_from, visited_cities, full_route, choose):
        available_routes = [route for route in connections[city_from] if route[0] not in visited_cities]
        if not available_routes:
            return [full_route, sum(full_route)]
        else:
            return choose([get_all_routes(route[0], visited_cities + [city_from], full_route + [route[1]], choose) for route in available_routes], key=lambda x: x[1])

    min_routes = []
    max_routes = []
    for city in connections.keys():
        min_routes.append(get_all_routes(city, [], [], min))
        max_routes.append(get_all_routes(city, [], [], max))
    print(min(min_routes, key=lambda x: x[1])[1])
    print(max(max_routes, key=lambda x: x[1])[1])

if __name__ == "__main__":
    main()
