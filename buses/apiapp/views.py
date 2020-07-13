from datetime import datetime

from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework import viewsets, generics

from apiapp.serializers import *
from mainapp.models import Company, Country, State


class CompaniesView(viewsets.ModelViewSet):
	queryset = Company.objects.filter(is_active=True)
	serializer_class = CompanySerializer


class CountriesView(viewsets.ModelViewSet):
	queryset = Country.objects.all()
	serializer_class = CountrySerializer


class CitesView(viewsets.ModelViewSet):
	queryset = City.objects.all()
	serializer_class = CitySerializer

	def get_queryset(self):
		return City.objects.filter(name__contains=self.request.query_params.get('city', ''))


class StatesView(viewsets.ModelViewSet):
	queryset = State.objects.all()
	serializer_class = StateSerializer


class TripsView(viewsets.ModelViewSet):
	queryset = Trip.objects.all()
	serializer_class = TripSerializer


class BusesView(viewsets.ModelViewSet):
	queryset = Bus.objects.all()
	serializer_class = BusSerializer


class SeatTypesView(viewsets.ModelViewSet):
	queryset = SeatType.objects.all()
	serializer_class = SeatTypeSerializer


class BusSeatsView(viewsets.ModelViewSet):
	queryset = BusSeat.objects.all()
	serializer_class = BusSeatSerializer


class CompanyView(viewsets.ModelViewSet):
	serializer_class = CompanySerializer

	def get_object(self):
		queryset = get_object_or_404(Company, is_active=True, pk=self.kwargs['company'])
		return queryset


class TripView(viewsets.ModelViewSet):
	serializer_class = TripSerializer

	def get_object(self):
		queryset = get_object_or_404(Trip, is_active=True, pk=self.kwargs['trip'])
		return queryset


class BusView(viewsets.ModelViewSet):
	serializer_class = BusSerializer

	def get_object(self):
		queryset = get_object_or_404(Bus, is_active=True, pk=self.kwargs['bus'])
		return queryset


class BusSeatView(viewsets.ModelViewSet):
	serializer_class = BusSeatSerializer

	def get_object(self):
		queryset = get_object_or_404(BusSeat, is_active=True, pk=self.kwargs['bus_seat'])
		return queryset


class FilterTripsView(viewsets.ModelViewSet):
	serializer_class = TripSerializer

	def get_queryset(self):
		queryset = Trip.objects.filter(
			departure_city__name__icontains=self.request.query_params.get('departure_city', ''),
			arrival_city__name__icontains=self.request.query_params.get('arrival_city', ''),
			departure_time__gte=datetime.strptime(
				self.request.query_params.get('departure_time', datetime.now()
				                              .strftime("%Y-%m-%d")),'%Y-%m-%d')
		)

		return queryset
