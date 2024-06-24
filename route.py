from address import Address

class Route:
    def __init__(self, route_number):
        self.route_number = route_number
        self.addresses = []

    def add_address(self, address):
        self.addresses.append(address)

    def __repr__(self):
        addresses_str = "\n  ".join(str(address) for address in self.addresses)
        return f"Route {self.route_number}:\n  {addresses_str}"

    def __iter__(self):
        return iter(self.addresses)

    @classmethod
    def from_file(cls, file_path):
        routes = []
        current_route = None

        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()

                if line.startswith("Маршрут №"):
                    route_number = line.split("№")[1].strip()
                    current_route = cls(route_number)
                    routes.append(current_route)

                elif line and current_route:
                    current_route.add_address(Address.parsing_point(line))

        return routes

if __name__ == "__main__":
    routes = Route.from_file('routes.txt')
    for route in routes:
        for address in route:
            print("Route number", route.route_number, ", Address",address)
