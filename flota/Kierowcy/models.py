from django.core.exceptions import ValidationError
from django.db import models

def PESEL_walidator(value):
    if len(value) != 11:
        raise ValidationError('PESEL 11 znaków !')
# Create your models here.
class Kierowcy(models.Model):
    PESEL = models.CharField(max_length=11, unique=True, validators=[PESEL_walidator])
    imie = models.CharField(max_length=32)
    nazwisko = models.CharField(max_length=32)
    data_zatrudnienia = models.DateField(null=True)

class PrawoJazdy(models.Model):
    kierowca = models.OneToOneField(Kierowcy, on_delete=models.CASCADE, primary_key=True, related_name="prawojazdy")
    data_waznosci = models.DateField()
    B = models.BooleanField(default=True)
    CE = models.BooleanField(default=True)
    C = models.BooleanField(default=True)
    BE = models.BooleanField(default=False)
    C1 = models.BooleanField(default=False)

class Kwalifikacja(models.Model):
    kierowca = models.OneToOneField(Kierowcy, on_delete=models.CASCADE, primary_key=True, related_name="kwalifikacja")
    data_waznosci = models.DateField()

class ADRdriver(models.Model):
    kierowca = models.OneToOneField(Kierowcy, on_delete=models.CASCADE, primary_key=True, related_name="adr")
    data_waznosci = models.DateField()
    kat1 = models.BooleanField(default=False)
    kat7 = models.BooleanField(default=False)


