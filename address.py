class Address:

    def __init__(self, main_address, second_address, garage_status):
        self.main_address = main_address #Адрес из маршрута
        self.second_address = second_address #Адрес из распреда, который по факту тот же, но может отличаться

    def __str__(self):
        return f"{self.main_address}, {self.second_address}"

