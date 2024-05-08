from django.shortcuts import render
from django.template.response import TemplateResponse
from django.http import HttpResponse
import requests
from .models import Artikel

def startseite(request):
    artikels = Artikel.objects.all()
    search = None

    if request.method == "POST":
        print(request)
        print(request.POST)
        search = Artikel.objects.get(titel = request.POST["suche"])

    ctx = {"artikels": artikels, "suche": search}

    return TemplateResponse(request, "ShopNest/startseite.html", ctx)

def artikelView(request, id):
    artikel = Artikel.objects.get(id=id)
    ctx = {"artikel": artikel}
    return TemplateResponse(request, "ShopNest/artikelView.html", ctx)


# def hello(request):
#     response_data = CallAPI()
#     for data in response_data:
#     Artikel.objects.create(titel = data['title'], preis = data['price'], beschreibung = data['description'], artikelkategorie = Artikelkategorie.objects.get(name = data['category']), bild = data['image'], bewertung = Bewertung.objects.create(rating_rate = data['rating']['rate'], rating_count = data['rating']['count']))
#     return TemplateResponse(request, "ShopNest/base.html")

def CallAPI():
    BASE_URL = "https://fakestoreapi.com"
    response = requests.get(f"{BASE_URL}/products")
    return response.json()

