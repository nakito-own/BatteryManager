from address import Address


class Robot:
    name = ''
    actual_location = Address
    garage_status = False
    gen = ''

    def __init__(self, name, address, garage_status, gen):
        self.gen = gen
        self.garage_status = garage_status
        self.name = name
        self.actual_location = address

    def __str__(self):
        return f"Name: {self.name}, Location: {self.actual_location}, Garage status: {'True' if self.garage_status else 'False'}, Generation: {'new' if int(self.name[1:]) > 390 else 'old'}"

    def __repr__(self):
        return f"Name: {self.name}, Location: {self.actual_location}, Garage status: {'True' if self.garage_status else 'False'}, Generation: {'new' if int(self.name[1:]) > 390 else 'old'}"

    def get_name(self):
        return self.name

    def get_actual_location(self):
        return self.actual_location

    def get_gen(self):
        return self.gen

    def get_info(self):
        return f"Name: {self.name}, Location: {self.actual_location}, Garage status: {self.garage_status}, Generation: {self.gen}"