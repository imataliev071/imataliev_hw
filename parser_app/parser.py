import requests
from bs4 import BeautifulSoup as bs
from django.views.decorators.csrf import csrf_exempt

URL = "https://kinogo.uk"

HEADERS = {
    "Accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/116.0"
}


# start
@csrf_exempt
def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS, params=params)
    return req


# get data
@csrf_exempt
def get_data(html):
    soup = bs(html, 'html.parser')
    items = soup.find_all('article', class_='card d-flex')
    kinogo_film = []

    for item in items:
        kinogo_film.append({
            "title": item.find("h2", class_='card__title').get_text(),
            "description": item.find("p", class_='card__text line-clamp').get_text(),
            "image": URL + item.find('a', class_='card__img img-fit-cover').find('img').get('src')
        })

    return kinogo_film




# endparser
@csrf_exempt
def parser_kinogo():
    html = get_html(URL)
    if html.status_code == 200:
        kinogo_film_2 = []
        for page in range(0, 1):
            html = get_html(f'https://kinogo.uk', params=page)
            kinogo_film_2.extend(get_data(html.text))
        return kinogo_film_2
        # print(kinogo_film_2)

    else:
        raise Exception('Error in Parse')


parser_kinogo()
