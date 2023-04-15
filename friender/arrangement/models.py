from django.db import models
from datetime import datetime


SEX = [
    ('m', 'male'),
    ('f', 'female')
]
CATEGORY = [
    ('r', 'restaurant'),
    ('c', 'cafe'),
    ('k', 'bar')
]
HOBBIES = [
    ('s', 'sport'),
    ('t', 'traveling'),

]


class Users(models.Model):
    name = models.CharField(max_length=10)
    surname = models.CharField(max_length=100)
    age = models.IntegerField()
    sex = models.CharField(max_length=1, choices=SEX)
    email = models.EmailField(null=True, unique=True)
    city = models.CharField(max_length=100, default='Minsk')

    def __str__(self):
        return self.name


class Passport(models.Model):
    passport_id = models.CharField(max_length=10, unique=True)
    date_create = models.DateTimeField(auto_created=datetime)
    user = models.OneToOneField('Users', on_delete=models.CASCADE)

    def __str__(self):
        return self.passport_id


class Hobbies(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=2, choices=HOBBIES)
    user = models.ManyToManyField('Users')

    def __str__(self):
        return self.name


class UserRating(models.Model):
    rating = models.PositiveIntegerField()
    description = models.CharField(max_length=255)
    user = models.ForeignKey('Users', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)


class Arrangements(models.Model):
    user1 = models.ForeignKey('Users', on_delete=models.CASCADE)
    # user2 = models.ForeignKey('Users', on_delete=models.CASCADE)
    establishments = models.ForeignKey('Establishments', on_delete=models.CASCADE)


class Establishments(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=1, choices=CATEGORY)

    def __str__(self):
        return self.name


class EstablishmentsRating(models.Model):
    rating = models.PositiveIntegerField()
    description = models.CharField(max_length=255)
    establishment = models.ForeignKey('Establishments', on_delete=models.CASCADE)

    def __str__(self):
        return self.establishment
