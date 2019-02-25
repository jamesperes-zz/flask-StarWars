import requests

def get_all_film():
    all_films = []
    data_all_films = requests.get('https://swapi.co/api/films/?format=json')
    all_films_json = data_all_films.json()
    for film in all_films_json['results']:
        all_films.append({'id': film['episode_id'], 'title': film['title']})
    return all_films


def get_films_by_person(list_films):
    films_participating = []
    films_not_participating = []
    all_films = get_all_film()

    for film in list_films:
        film_data = requests.get(film).json()
        films_participating.append({'id': film_data['episode_id'], 'title': film_data['title']})

    for film in all_films:
        if film not in films_participating:
            films_not_participating.append(film)
    
    return films_not_participating


def get_person_films_not_participated(id):
    url   = f'https://swapi.co/api/people/{id}/?format=json'
    data  = requests.get(url)
    films = data.json()['films']
    films_participating = get_films_by_person(films)
    return films_participating