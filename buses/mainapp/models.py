from django.db import models


# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=255, verbose_name="Company")
    rating = models.IntegerField(verbose_name="Company's rating", default=0)
    description = models.TextField(max_length=9999, verbose_name="Company's description", default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class State(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, verbose_name="Country", on_delete=models.CASCADE)


class City(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.ForeignKey(Country, verbose_name="Country", on_delete=models.CASCADE)
    state = models.ForeignKey(State, verbose_name="State", on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=20, decimal_places=7)
    longitude = models.DecimalField(max_digits=20, decimal_places=7)

    def __str__(self):
        return self.name


class Bus(models.Model):
    name = models.CharField(max_length=50, verbose_name="Bus name")
    company = models.ForeignKey(Company, verbose_name="Company", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Trip(models.Model):
    departure_city = models.ForeignKey(City, related_name="from+", verbose_name="From", on_delete=models.CASCADE)
    arrival_city = models.ForeignKey(City, related_name="to+", verbose_name="To", on_delete=models.CASCADE)
    company = models.ForeignKey(Company, verbose_name="Company", on_delete=models.CASCADE)
    bus = models.ForeignKey(Bus, verbose_name="Select a bus", on_delete=models.CASCADE)
    departure_time = models.DateTimeField(verbose_name="Departure time")
    arrival_time = models.DateTimeField(verbose_name="Arrival time")
    starting_price = models.DecimalField(decimal_places=2, max_digits=7, verbose_name="Seat price", default=0.00)

    def __str__(self):
        return f'{self.departure_city.name} - {self.arrival_city.name}'


class SeatType(models.Model):
    company = models.ForeignKey(Company, verbose_name="Company", on_delete=models.CASCADE)
    name = models.CharField(max_length=30, verbose_name="Seat name")
    price = models.DecimalField(decimal_places=2, max_digits=7, verbose_name="Seat price")

    def __str__(self):
        return self.name


class BusSeat(models.Model):
    seat_type = models.ForeignKey(SeatType, verbose_name="Company", on_delete=models.CASCADE)
    bus = models.ForeignKey(Bus, verbose_name="Select a bus", on_delete=models.CASCADE)

    def __str__(self):
        return self.seat_type.name
