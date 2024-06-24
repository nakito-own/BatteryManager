import re

class Address:
    def __init__(self, points):
        self.points = points

    def get_addresses(self):
        return self.points

    def __repr__(self):
        return f"Addresses: {self.points}"

    def __iter__(self):
        return iter(self.points)

    @classmethod
    def parsing_point(cls, address_string):
        if address_string.startswith("•"):
            points = [address_string.split("storage: ")[1].strip()]
        else:
            match = re.search(r'\) - (.*)', address_string)
            if match:
                address_part = match.group(1)
                addresses = re.split(r'\(|\)', address_part)
                points = [address.strip() for address in addresses if address.strip()]
            else:
                points = []

        return cls(points)
