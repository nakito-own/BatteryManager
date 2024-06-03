from distribution import Distribution
from route import Route


class BatteryCounter:
    def __init__(self, routes, distribution):
        self.routes = routes
        self.distribution = distribution

    def match_robots_to_routes(self):
        matches = {}

        for route in self.routes:
            route_number = route.route_number
            matches[route_number] = []

            for address in route.addresses:
                for robot, robot_address in self.distribution.assignments:
                    print(f"Comparing route address: {address} with robot address: {robot_address}")
                    if (address.main_address == robot_address.main_address and
                            address.second_address == robot_address.second_address):
                        matches[route_number].append(robot)
                        print(f"Match found: {robot} for route {route_number}")

        return matches

    def __str__(self):
        result = []
        matches = self.match_robots_to_routes()

        for route_number, robots in matches.items():
            result.append(f"Route {route_number}:")
            for robot in robots:
                result.append(f"  {robot}")

        return "\n".join(result)


if __name__ == "__main__":
    routes = Route.from_file('routes.txt')
    distribution = Distribution.from_file("distribution.txt")

    # Проверка данных маршрутов
    if not routes:
        print("No routes found.")
    else:
        print("Loaded routes:")
        for route in routes:
            print(route)

    # Проверка данных распределения
    if not distribution.assignments:
        print("No robot assignments found.")
    else:
        print("Loaded robot assignments:")
        for robot, address in distribution.assignments:
            print(f"{robot} - {address}")

    matcher = BatteryCounter(routes, distribution)
    print(matcher)
