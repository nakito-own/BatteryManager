class Address:
    def __init__(self, main_address, second_address=''):
        self.coordinates = ''
        self.main_address = main_address
        self.second_address = second_address

    def __str__(self):
        return f"{self.main_address} ({self.second_address})" if self.second_address else self.main_address

    def get_main_address(self):
        return self.main_address

    def get_second_address(self):
        return self.second_address

    def get_coordinates(self):
        return self.coordinates
