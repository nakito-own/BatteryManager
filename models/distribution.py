from models.robot import Robot
from models.address import Address
from models.route import Route


class Distribution:
    def __init__(self):
        self.robots = None
        self.assignments = []

    def add_assignment(self, robot):
        self.assignments.append((robot))

    def __str__(self):
        return "\n".join([f"{robot}" for robot in self.assignments])

    def __repr__(self):
        return f"{self.robots}"

    @classmethod
    def from_file(cls, file_path):
        distribution = cls()
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line.startswith("•"):
                    parts = line.split(",")
                    name = parts[0].strip().split(" ")[1]
                    garage_status = "гараж" in line
                    gen = 'new' if int(name[1:]) > 390 else 'old'

                    address = Address.parsing_point(line)

                    robot = Robot(name, address, garage_status, gen)
                    distribution.add_assignment(robot)
        return distribution

    def find_robot_by_address(self, address):

        found_robots = []
        addresses = address
        for found_location in addresses:
            for robot in self.assignments:
                robot_location = Address.get_addresses(robot.get_actual_location())[0]
                if robot_location == found_location:
                    found_robots.append(robot)

        return found_robots


if __name__ == "__main__":
    distribution = Distribution.from_file("input-files/distribution.txt")
    routes = Route.from_file('input-files/routes.txt')

    print(distribution)

    print(distribution.find_robot_by_address(Address(['Лесная, 5'])))