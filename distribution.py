from robot import Robot
from address import Address
from route import Route
class Distribution:
    def __init__(self):
        self.assignments = []

    def add_assignment(self, robot, address):
        self.assignments.append((robot, address))

    def __str__(self):
        return "\n".join([f"{robot} - {address}" for robot, address in self.assignments])

    @classmethod
    def from_file(cls, file_path):
        distribution = cls()
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line.startswith("•"):
                    parts = line.split(", storage: ")
                    name = parts[0].strip().split(" ")[1]
                    storage_info = parts[1].strip()
                    garage_status = "гараж" in storage_info
                    gen = 'new' if int(name[1:]) > 390 else 'old'
                    address = Address(storage_info)
                    robot = Robot(name, address, garage_status, gen)
                    distribution.add_assignment(robot, address)
        return distribution

    def find_robot_by_address(self, address):
        if not isinstance(address, Address):
            raise TypeError("Argument must be an instance of Address")

        found_robots = [
            robot for robot, addr in self.assignments
            if (addr.get_main_address() == address.get_main_address() or
                addr.get_main_address() == address.get_second_address())
        ]
        return found_robots

if __name__ == "__main__":
    distribution = Distribution.from_file("distribution.txt")
    routes = Route.from_file('routes.txt')

    for route in routes:
        for address in route:
            print(distribution.find_robot_by_address(address))
    print(distribution)

    main_address = "Лавка на Смоленском"
    search_address = Address(main_address)
    robots_at_address = distribution.find_robot_by_address(search_address)
    for robot in robots_at_address:
        print(robot)
