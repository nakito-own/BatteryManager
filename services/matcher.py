from models.distribution import Distribution
from models.route import Route

distribution = Distribution.from_file('input-files/distribution.txt')
routes = Route.from_file('input-files/routes.txt')

def matcher(distribution, routes):

    for route in routes:
        for address in route:

            found_robot = []
            found_robot.append(distribution.find_robot_by_address(address))
            print('Маршрут номер:', route.route_number, 'Адрес на маршруте:', address, 'Найдены роботы:', found_robot)


matcher(distribution, routes)