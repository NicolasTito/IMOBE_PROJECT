from django.db import models
from django.contrib.auth.models import User

class Image(models.Model):
    img = models.ImageField(upload_to='img')

    def __str__(self) -> str:
        return self.img.url


class City(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name


class DaysVisits(models.Model):
    day = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.day


class Schedule(models.Model):
    schedule = models.TimeField()

    def __str__(self) -> str:
        return str(self.schedule)


class Property(models.Model):
    choices = (('S', 'Sale'),
               ('R', 'Rent'))

    choices_property = (('A', 'Apartment'),
                        ('H', 'House'))

    image = models.ManyToManyField(Image)
    value = models.FloatField()
    room = models.IntegerField()
    size = models.FloatField()
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING)
    street = models.CharField(max_length=50)
    type = models.CharField(max_length=1, choices=choices)
    type_property = models.CharField(max_length=1, choices=choices_property)
    number = models.IntegerField()
    description = models.TextField()
    days_visits = models.ManyToManyField(DaysVisits)
    schedule = models.ManyToManyField(Schedule)

    def __str__(self) -> str:
        return self.street


class Visits(models.Model):
    choices = (('M', 'Monday'),
               ('TU', 'Tuesday'),
               ('W', 'Wednesday'),
               ('TH', 'Thursday'),
               ('F', 'Friday'),
               ('SA', 'Saturday'),
               ('Su', 'Sunday'))
    choices_status = (('S', 'Scheduled'),
                      ('F', 'Finished'),
                      ('C', 'Canceled'))
    property = models.ForeignKey(Property, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    day = models.CharField(max_length=20)
    schedule = models.TimeField()
    status = models.CharField(max_length=1, choices=choices_status, default="S")
