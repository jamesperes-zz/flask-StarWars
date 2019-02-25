import requests

def get_all_film():
    all_films = []
    data_all_films = requests.get('https://swapi.co/api/films/?format=json')
    all_films_json = data_all_films.json()
    for film in all_films_json['results']:
        all_films.append({'id': film['episode_id'], 'title': film['title']})
    return all_films


def get_films_by_person(list_films):
    films_showed = []
    films_not_showed = []
    all_films = get_all_film()

    for film in list_films:
        film_data = requests.get(film).json()
        films_showed.append({'id': film_data['episode_id'], 'title': film_data['title']})

    for film in all_films:
        if film not in films_showed:
            films_not_showed.append(film)
    
    return films_not_showed


def get_person(id):
    url   = f'https://swapi.co/api/people/{id}/?format=json'
    data  = requests.get(url)
    films = data.json()['films']
    films_showed = get_films_by_person(films)
    return films_showed