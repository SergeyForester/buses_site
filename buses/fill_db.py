# coding:utf-8
import datetime
import time
from pprint import pprint

import django
import requests
import json

from mainapp.models import City, Country, State

from geopy.geocoders import Nominatim

# fetching data
data = json.loads(requests.get(
	"https://pkgstore.datahub.io/core/world-cities/world-cities_json/data/5b3dd46ad10990bca47b04b4739a02ba/world-cities_json.json").content)
print("Data: " + str(data)[:100])

# iterating through list

cities_counter = 0
geolocator = Nominatim(user_agent="fill_db")

for element in data:
	if City.objects.filter(country__name=element['country'], name=element['name']):
		continue

	# looking for a country
	try:
		country = Country.objects.get(name=element['country'])
	except Country.DoesNotExist:
		# if the country does not exist -> create it
		country = Country.objects.create(name=element['country'])

	# looking for coordinates
	location = geolocator.geocode(f"{element['country']}, {element['name']}", addressdetails=True)
	if location:
		latitude, longitude = location.latitude, location.longitude

		address = location.raw['address']

		if 'state' in address:
			state = location.raw['address']['state']
		elif 'municipality' in address:
			state = location.raw['address']['municipality']
		else:
			state = ""
	else:
		latitude, longitude = 0.000, 0.0000
		state = ""

	# looking for a state
	try:
		state = State.objects.get(name=state, country=country)
	except State.DoesNotExist:
		state = State.objects.create(name=state, country=country)

	# trying to create city
	try:
		City.objects.create(country=country, name=element['name'],
		                    state=state, latitude=round(latitude, 7), longitude=round(longitude, 7))
	except (City.DoesNotExist, django.db.utils.IntegrityError):
		pass

	cities_counter += 1
	print(f"City №{cities_counter}")

print("Cities created: " + str(cities_counter))
