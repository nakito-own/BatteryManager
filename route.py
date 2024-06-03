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
                    # Извлечение основной и дополнительной части адреса
                    address_part = line.split(") - ", 1)[1]
                    if '(' in address_part:
                        main_address, second_address = address_part.split('(', 1)
                        main_address = main_address.strip()
                        second_address = second_address.rstrip(')').strip()
                    else:
                        main_address = address_part.strip()
                        second_address = ''

                    address = Address(main_address, second_address)
                    current_route.add_address(address)

        return routes

if __name__ == "__main__":
    routes = Route.from_file('routes.txt')

    for route in routes:
        print(route)

