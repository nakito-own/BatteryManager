from robot import Robot
from address import Address


class Distribution:
    def __init__(self):
        self.assignments = []

    def add_assignment(self, robot, address):
        self.assignments.append((robot, address))

    def __str__(self):
        return "\n".join([f"{robot.get_name()} - {address.main_address}" for robot, address in self.assignments])

    @classmethod
    def from_file(cls, file_path):
        distribution = cls()

        current_address = None

        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()

                if line.startswith("•"):

                    parts = line.split(",")
                    name = parts[0].strip().split(" ")[1]
                    garage_status = "гараж" in line

                    storage_info = line.split("storage: ")[1].strip()
                    address = Address(storage_info)

                    robot = Robot(name, address, garage_status)
                    distribution.add_assignment(robot, address)

        return distribution

if __name__ == "__main__":
    distribution = Distribution.from_file("distribution.txt")
    print(distribution)

