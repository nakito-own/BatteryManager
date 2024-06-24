
from distribution import Distribution
from route import Route

distribution = Distribution.from_file('distribution.txt')
routes = Route.from_file('routes.txt')

def matcher(distribution, routes):

    matches = []
    for route in routes:
        print("Прочесываем маршрут номер", route.route_number)
        for address in route:
            print("Прочесываем этот адрес: ", address)
            robots = distribution.find_robot_by_address(address)
            print("На этом адресе найдены роботы: ", robots)
            if robots:
                matches.append((address, robots))
    return matches

results = matcher(distribution, routes)
print(results)
