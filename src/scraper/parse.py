import pprint
import json
from bs4 import BeautifulSoup


class Parser:
    def __init__(self, source):
        self.source = source

    def parse(self):
        films = []
        with open(self.source, "rb") as f:
            soup = BeautifulSoup(f.read(), "html.parser")
            films_soup = soup.find_all("div", attrs={"class": "movieItem_info"})
            for film in films_soup:
                new_film = {}

                new_film["title"] = film.find_next("a", attrs={"class": "movieItem_title"}).get_text()

                description = film.find_next("span", attrs={"class": "movieItem_subtitle"})
                new_film["description"] = "" if description is None else description.get_text()

                new_film["genre"] = film.find_next("span", attrs={"class": "movieItem_genres"}).get_text()
                new_film["year"], new_film["country"] = film.find_next("span", attrs={"class": "movieItem_year"}).get_text().split(", ")
                new_film["link"] = film.find_next("a", attrs={"class": "movieItem_button movieItem_button-tickets button-warning"}).attrs["href"]
                new_film["rating"] = float(film.find_next("span", attrs={"class": "mark_num"}).get_text())
                films.append(new_film)
        return films

    def save(self, path):
        with open(path, 'w') as f:
            f.write(json.dumps(self.parse(), indent=4))

