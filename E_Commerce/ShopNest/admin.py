from django.contrib import admin
from .models import User, Adresse, Bewertung, Bestellung, BestellteArtikel, Artikel, Artikelkategorie
from django.contrib.auth.admin import UserAdmin

admin.site.register(User)
admin.site.register(Bewertung)
admin.site.register(Adresse)
admin.site.register(Bestellung)
admin.site.register(BestellteArtikel)
admin.site.register(Artikel)
admin.site.register(Artikelkategorie)
