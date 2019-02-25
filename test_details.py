import unittest
from details import get_all_film, get_films_by_person, get_person_films_not_participated

class DetailTestes(unittest.TestCase):
    def test_get_all_film(self):
        all_films = get_all_film()
        self.assertEqual(len(all_films), 7)

    def test_get_films_by_person(self):
        list_films = ["https://swapi.co/api/films/7/"]
        films_by_person = get_films_by_person(list_films)
        self.assertEqual(len(films_by_person), 6)

    def test_get_person_films_not_participated(self):
        person = get_person_films_not_participated(1)
        self.assertEqual(len(person), 2)