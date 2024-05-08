# E-Commerce-Website

1. language: german

## Tools
1. Python 12
2. Django
3. MySQL
4. Bootstrap5
5. Django-Debug-Toolbar
6. Django-Money

## Installation
1. virtuelle Umgebung erstellen mit folgendem Befehl: python -m venv <name der umgebung>
2. Umgebung aktivieren mit dem Befehl: <name der umgebung>/Scripts/activate
3. requirements installieren mit dem Befehl: pip install -r requirements.txt
4. Bootstrap CDN in das Base Template im head-Tag einfügen. Hier ist der Pfad zum Base-File: E_Commerce/ShopNest/templates/ShopNest/base.html
5. Erstelle im Übergeordneten Ordner eine ".env" Datei und weise deinen Datenbank Namen, Passwort und Usernamen für die Varibalen in der settings Datei zu.
6. Fülle die Datenbank mit Inhalten deiner wahl
7. Gebe folgenden Befehl im Terminal ein: python manage.py runserver
