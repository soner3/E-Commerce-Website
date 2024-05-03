from djmoney.models.fields import MoneyField
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    geburtstag = models.DateField(null=True, blank=True)
    profilbild = models.URLField(null=True, blank=True)

    def __str__(self) -> str:
        return self.username

class Adresse(models.Model):
    strasse = models.CharField(max_length=255)
    hausnummer = models.CharField(max_length=50)
    plz = models.CharField(max_length=20)
    land = models.CharField(max_length=50)
    stadt = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Artikelkategorie(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name



class Bewertung(models.Model):
    rating_rate = models.FloatField(default=0)
    rating_count = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return str(self.rating_rate)

class Artikel(models.Model):
    titel = models.CharField(max_length=255)
    preis = models.DecimalField(max_digits=10, decimal_places=2)
    beschreibung = models.TextField()
    bild = models.URLField(null=True, blank=True)

    artikelkategorie = models.ForeignKey(Artikelkategorie, on_delete=models.CASCADE)
    bewertung = models.ForeignKey(Bewertung, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return self.titel


class Bestellung(models.Model):
    gesamtsumme = MoneyField(max_digits=15, decimal_places=2, default_currency="EUR")
    status = models.CharField(max_length=50)
    datum = models.DateTimeField(auto_now_add=True)
    bestellnummer = models.CharField(max_length=50)
    zahlungsart = models.CharField(max_length=100)
    artikelanzahl = models.IntegerField()

    artikel = models.ManyToManyField(Artikel, through="BestellteArtikel")
    adresse = models.ForeignKey(Adresse, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.bestellnummer

class BestellteArtikel(models.Model):
    artikel = models.ForeignKey(Artikel, on_delete=models.CASCADE)
    bestellung = models.ForeignKey(Bestellung, on_delete=models.CASCADE)


    





