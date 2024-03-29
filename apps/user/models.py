from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Role(models.Model):
    reference = models.CharField(max_length=25)
    nombre = models.CharField(max_length=25)

    def __str__(self):
        return '{}'.format(self.nombre)


class User(AbstractUser):
    code = models.CharField(max_length=10, unique=True)
    username = models.CharField(max_length=150, unique=False)
    first_name = models.CharField(max_length=45)
    password = models.CharField(max_length=128)
    last_name = models.CharField(max_length=25)
    second_last_name = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=45)
    phone = models.CharField(max_length=15)
    filename = models.FileField(upload_to='', default='no.jpg')
    role = models.ForeignKey(Role, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {} {}'.format(self.first_name, self.last_name, self.second_last_name)
