class Route:
    def __init__(self, route_number):
        self.route_number = route_number
        self.addresses = []

    def add_address(self, address):
        self.addresses.append(address)

    def __repr__(self):
        return f"Route {self.route_number}: {self.addresses}"

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
                    # Extracting the address part after the time range
                    address = line.split(") - ", 1)[1]
                    current_route.add_address(address)

        return routes

