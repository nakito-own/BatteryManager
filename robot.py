from address import Address


class Robot:
    name = ''
    actual_location = Address
    garage_status = False
    gen = ''

    def __init__(self, name, actual_location, garage_status, gen):
        self.name = name
        self.actual_location = actual_location
        self.garage_status = garage_status
        self.gen = gen

    def __str__(self):
        return f"Name: {self.name}, Location: {self.actual_location}, Garage status: {'в гараже' if self.garage_status else 'не в гараже'}, Generation: {'new' if int(self.name[1:]) > 390 else 'old'}"

    def get_name(self):
        return self.name

    def get_actual_location(self):
        return self.actual_location

    def get_gen(self):
        return self.gen

    def get_info(self):
        return self.name, self.garage_status, self.gen