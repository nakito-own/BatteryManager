class Address:
    def __init__(self, main_address, second_address=''):
        self.main_address = main_address.strip()
        self.second_address = second_address.strip()

    def get_main_address(self):
        return self.main_address

    def get_second_address(self):
        return self.second_address

    def __repr__(self):
        return f"Main address: {self.main_address}, Second address: {self.second_address}"
