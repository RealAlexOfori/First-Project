from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.city import City
import repositories.city_repository as city_repository

cities_blueprint = Blueprint("cities", __name__)

@cities_blueprint.route("/cities")
def cities():
    cities = city_repository.select_all() # NEW
    return render_template("cities/index.html", all_cities = cities)

# NEW
# GET '/cities/new'
@cities_blueprint.route("/cities/new", methods=['GET'])
def new_city():
    cities = city_repository.select_all()
    return render_template("cities/new.html", all_cities = cities)

# CREATE
# POST '/cities'
@cities_blueprint.route("/cities",  methods=['POST'])
def create_city():
    name = request.form['name']
    visited   = request.form.get('visited') == 'visited'
    city        = City(name, visited)
    city_repository.save(city)
    return redirect('/cities')


# SHOW
# GET '/cities/<id>'
@cities_blueprint.route("/cities/<id>", methods=['GET'])
def show_city(id):
    city = city_repository.select(id)
    return render_template('cities/show.html', city = city)

# EDIT
# GET '/cities/<id>/edit'
@cities_blueprint.route("/cities/<id>/edit", methods=['GET'])
def edit_country(id):
    city = city_repository.select(id)
    cities = city_repository.select_all()
    return render_template('cities/edit.html', city = city, all_cities = cities)

# UPDATE
# PUT '/cities/<id>'
@cities_blueprint.route("/cities/<id>", methods=['POST'])
def update_city(id):
    name = request.form['name']
    visited    = request.form['visited']
    city_id     = request.form['city_id']
    city        = city_repository.select(city_id)
    city        = City(name,visited, city,id)
    city_repository.update(city)
    return redirect('/cities')

#DELETE
#DELETE '/cities/<id>'
@cities_blueprint.route("/cities/delete", methods=['POST'])
def delete_city():
    id = request.form["city_id"]
    city_repository.delete(id)
    return redirect('/cities')


# @cities_blueprint.route('/cities/delete', methods=['POST'])
# def remove_city():
#   city_to_be_removed = [city for city in cities if city.name == request.form["city_to_remove"]]
#   cities.remove(city_to_be_removed[0])

#   return redirect('/cities')
