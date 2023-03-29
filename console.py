from models.city import City
import repositories.city_repository as city_repository
# import pdb

city1 = City("Accra", False)
city_repository.save(city1)

city2 = City("Lisbon", False)
city_repository.save(city2)

city3 = City("New York", False)
city_repository.save(city3)

city4 = City("Jerusalem", False)
city_repository.save(city4)

city5 = City("Cairo", False)
city_repository.save(city5)

cities = city_repository.select_all()

# pdb.set_trace()

# print(f"there are {len(cities)} cities")

# cities_id = [city.id for city in cities]

# print("valid city ids:")

# for id in cities_id:
#     print(id)

# city_repository.delete((cities_id[0]))

# cities = city_repository.select_all()

# print(f"there are {len(cities)} cities")
