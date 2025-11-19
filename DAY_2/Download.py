import requests
from bs4 import BeautifulSoup
from PIL import Image

adres_strony = 'https://www.olx.pl/motoryzacja/samochody/'

#pobieramy źródło strony do zmiennej
zrodlo_strony = requests.get(adres_strony).content

#tworzymy parser BeautifulSoup z podanego źródła strony dzięki temu będziemy mieli łatwy dostęp do znaczników HTML
parser = BeautifulSoup(zrodlo_strony, 'html.parser')

#wyszukujemy wszystkie znaczniki <img> w źródle strony
obrazki = parser.find_all('img')
for img in obrazki:
    adres = img.get('src')
    nazwa = img.get('alt')

    if 'https://' not in adres:
        continue

    nazwa = nazwa.replace('/','-').replace(' ', '-')
    dane_obrazka = requests.get(adres).content

    os.makedirs('obrazki', exist_ok=True)

    with open('obrazki/' + nazwa + '.jpg', 'wb') as f:
        f.write(dane_obrazka)