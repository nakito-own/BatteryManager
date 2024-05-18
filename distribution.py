class Distribution:

    
    def __init__(self):
        self.locations = {}

    def add_robot_location(self, robot_id, location):
        if location not in self.locations:
            self.locations[location] = []
        self.locations[location].append(robot_id)

    def __repr__(self):
        return f"Distribution(locations={self.locations})"

    @classmethod
    def from_file(cls, file_path):
        distribution = cls()
        current_location = None

        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()

                if line.startswith("📍"):
                    current_location = line.split("📍")[1].strip()

                elif line.startswith("•"):
                    robot_id = line.split(",")[0].strip()
                    distribution.add_robot_location(robot_id, current_location)

        return distribution
