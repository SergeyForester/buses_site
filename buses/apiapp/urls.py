from django.urls import path, include
from rest_framework import routers

from apiapp import views

app_name = "apiapp"

router = routers.DefaultRouter()
router.register('v1/get/companies', views.CompaniesView)
router.register('v1/get/countries', views.CountriesView)
router.register('v1/get/states', views.StatesView)
router.register('v1/get/cities', views.CitesView)
router.register('v1/get/trips', views.TripsView)
router.register('v1/get/buses', views.BusesView)
router.register('v1/get/seat_types', views.SeatTypesView)
router.register('v1/get/bus_seats', views.BusSeatsView)

urlpatterns = [
	path('v1/get/companies/', views.CompaniesView.as_view({'get': 'list'})),
	path('v1/get/countries/', views.CountriesView.as_view({'get': 'list'})),
	path('v1/get/states/', views.StatesView.as_view({'get': 'list'})),
	path('v1/get/cities/', views.CitesView.as_view({'get': 'list'})),
	path('v1/get/trips/', views.TripsView.as_view({'get': 'list'})),
	path('v1/get/buses/', views.BusesView.as_view({'get': 'list'})),
	path('v1/get/seat_types/', views.SeatTypesView.as_view({'get': 'list'})),
	path('v1/get/bus_seats/', views.BusSeatsView.as_view({'get': 'list'})),

	path('v1/get/company/<int:company>/', views.CompanyView.as_view({'get': 'retrieve'}), name="company"),
	path('v1/get/trip/<int:trip>/', views.TripView.as_view({'get': 'retrieve'}), name="company"),
	path('v1/get/bus/<int:bus>/', views.BusView.as_view({'get': 'retrieve'}), name="company"),
	path('v1/get/bus_seat/<int:bus_seat>/', views.BusSeatView.as_view({'get': 'retrieve'}), name="company"),

	path('v1/filter/trips/', views.FilterTripsView.as_view({'get':'list'}))
	# path('', include(router.urls)),

]
