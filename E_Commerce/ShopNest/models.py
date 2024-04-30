from djmoney.models.fields import MoneyField
from django.db import models
from django.contrib.auth.models import AbstractUser

ARTIKEL_KATEGORIEN = (
    (1, "Lebensmittel"),
    (2, "Getränke"),
    (3, "Kleidung"),
    (4, "Haushaltswaren"),
    (5, "Backwaren"),
    (6, "Werkzeuge"),
    (7, "Möbel"),
    (8, "Küche"),
    (9, "Bücher"),
    (10, "Sport"),
    (11, "Technik"),
    (12, "Sonstiges"),
    (13, "Drogerieartikel"),
    (14, "Snacks und Süßigkeiten"),
)

BESTELLUNG_STATUS = (
    (1, "Bestellt"),
    (2, "In Bearbeitung"),
    (3, "In Lieferung"),
    (4, "Abgeschlossen"),
    (5, "Abgelehnt"),
    (6, "Storniert"),
)

ZAHLUNG = (
    (1,"Kreditkarte"),
    (2,"PayPal"),
    (3,"Lastschrift"),
    (4, "Klarna"),
)

class User(AbstractUser):
    geburtstag = models.DateField(null=True, blank=True)
    profilbild = models.ImageField(upload_to='profilbilder/ShopNest/', null=True, blank=True)

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
    name = models.CharField(choices=ARTIKEL_KATEGORIEN, max_length=50)

    def __str__(self) -> str:
        return self.name


class Artikel(models.Model):
    name = models.CharField(max_length=255)
    beschreibung = models.TextField()
    preis = MoneyField(max_digits=10, decimal_places=2, default_currency="EUR")
    bild = models.ImageField()
    artikelnummer = models.CharField(max_length=255)
    artikelkategorie = models.ForeignKey(Artikelkategorie, on_delete=models.CASCADE)
    anzahl = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.name

class Bewertung(models.Model):
    bewertung = models.IntegerField()
    kommentar = models.TextField()
    datum = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    artikel = models.ForeignKey(Artikel, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.bewertung

class Bestellung(models.Model):
    gesamtsumme = MoneyField(max_digits=15, decimal_places=2, default_currency="EUR")
    status = models.CharField(choices=BESTELLUNG_STATUS, max_length=50)
    datum = models.DateTimeField(auto_now_add=True)
    bestellnummer = models.CharField(max_length=50)
    zahlungsart = models.CharField(choices=ZAHLUNG, max_length=50)
    artikelanzahl = models.IntegerField()

    artikel = models.ManyToManyField(Artikel, through="BestellteArtikel")
    adresse = models.ForeignKey(Adresse, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.bestellnummer

class BestellteArtikel(models.Model):
    artikel = models.ForeignKey(Artikel, on_delete=models.CASCADE)
    bestellung = models.ForeignKey(Bestellung, on_delete=models.CASCADE)


    





