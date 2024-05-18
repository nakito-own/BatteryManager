from route import Route
from distribution import Distribution

# Тестик
routes = Route.from_file('routes.txt')
distribution = Distribution.from_file('distribution.txt')

for route in routes:
    print(route)

print(distribution)