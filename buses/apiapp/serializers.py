from rest_framework import serializers

from mainapp.models import Company, Country, State, City, Trip, Bus, SeatType, BusSeat


class CompanySerializer(serializers.ModelSerializer):
	class Meta:
		model = Company
		fields = ('id', 'name', 'description', 'is_active')


class CountrySerializer(serializers.ModelSerializer):
	class Meta:
		model = Country
		fields = ('id', 'name')


class StateSerializer(serializers.ModelSerializer):
	class Meta:
		model = State
		fields = ('id', 'name', 'country')


class CitySerializer(serializers.ModelSerializer):
	class Meta:
		model = City
		fields = ('id', 'name', 'state', 'country', 'latitude', 'longitude')


class TripSerializer(serializers.ModelSerializer):
	departure_city = CitySerializer(read_only=True)
	arrival_city = CitySerializer(read_only=True)
	company = CompanySerializer(read_only=True)

	class Meta:
		model = Trip
		fields = ('id', 'departure_city', 'arrival_city', 'company', 'bus', 'departure_time',
		          'arrival_time', 'starting_price')


class BusSerializer(serializers.ModelSerializer):
	class Meta:
		model = Bus
		fields = ('id', 'name', 'company')


class SeatTypeSerializer(serializers.ModelSerializer):
	class Meta:
		model = SeatType
		fields = ('id', 'name', 'company', 'price')


class BusSeatSerializer(serializers.ModelSerializer):
	class Meta:
		model = BusSeat
		fields = ('id', 'seat_type', 'bus')
