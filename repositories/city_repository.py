from db.run_sql import run_sql
from models.city import City


def save(city):
    sql = "INSERT INTO cities (name,visited) VALUES (%s,%s) RETURNING *"
    values = [city.name, city.visited]
    results = run_sql(sql, values)
    id = results[0]['id']
    city.id = id
    return city


def select_all():
    cities = []

    sql = "SELECT * FROM cities"
    results = run_sql(sql)

    for row in results:
        city = City(row['name'],row['visited'], row['id'] )
        cities.append(city)
    return cities


# delete_all()
def delete_all():
    sql ="DELETE * FROM cities"
    run_sql(sql)

def delete(id):
    sql ="DELETE FROM cities WHERE id = %s"
    values = [id]
    run_sql(sql, values)


# find_city_by_id -  select(id)
def select(id):
    city = None
    sql = "SELECT * FROM cities WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        city = City(result["name"],result["visited"], result["id"])
        # Q -  instead of  result["id"] can we use id?
    return city     
