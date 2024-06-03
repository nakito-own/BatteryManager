from address import Address
from route import Route

routes = Route.from_file('routes.txt')

for route in routes:
    print(route)

