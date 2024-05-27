from address import Address


class Robot:
    name = ''
    actual_location = Address
    garage_status = False

    def __init__(self, name, actual_location, garage_status):
        self.name = name
        self.actual_location = actual_location
        self.garage_status = garage_status

    def __str__(self):
        return f"{self.name}, {self.actual_location}, {'в гараже' if self.garage_status else 'не в гараже'}"

    def get_name(self):
        return f"{self.name}"

    def get_actual_location(self):
        return f"{self.actual_location}"
