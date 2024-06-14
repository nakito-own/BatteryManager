from address import Address
from distribution import Distribution
from route import Route

distribution = Distribution.from_file('distribution.txt')
routes = Route.from_file('routes.txt')

def matcher(distribution, routes):
    matches = []
    for route in routes:
        print(route)
        for address in route.addresses:
            print("Прочесываем этот адрес: ", address)

            robots = distribution.find_robot_by_address(address)
            print("На этом адресе найдены роботы: ", )
            if robots:
                matches.append((address, robots))
    return matches

results = matcher(distribution, routes)
for address, robots in results:
    print(f"Address: {address}")
    for robot in robots:
        print(f"  Robot: {robot}")
