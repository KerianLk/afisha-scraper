from download import Downloader
from parse import Parser
from data import Data
import datetime


def process(url, web_page_path, data_path):
    downloader = Downloader(url, params=PARAMS)
    downloader.save(web_page_path)

    parser = Parser(web_page_path)

    parser.save(data_path)

    data = Data(data_path)
    data.load_file()
    data.parse_json()

    if key == 'all' or key == '':
        for film in data.get_all_titles():
            print(*film, sep="\n")
            print()
    elif key == 'best':
        for film in data.get_best_films():
            print(*film, sep="\n")
            print()
    elif key == 'worst':
        for film in data.get_worst_films():
            print(*film, sep="\n")
            print()
    elif key == 'year':
        inp_year = input("Get films released in (year): ")
        for film in data.get_by_year(inp_year):
            print(*film, sep="\n")
            print()
    elif key == 'country':
        inp_country = input("Get films released in (country): ")
        for film in data.get_by_country(inp_country):
            print(*film, sep="\n")
            print()
    data.save_to_txt("file.txt")
    return data.get_all_titles()


genres_list = {
    0: 'Анимация',
    1: 'аниме',
    2: 'балет',
    3: 'биография',
    4: 'боевик',
    5: 'вестерн',
    6: 'военный',
    7: 'детектив',
    8: 'детский',
    9: 'документальный',
    10: 'драма',
    11: 'исторический',
    12: 'комедия',
    13: 'концерт',
    14: 'короткометражный',
    15: 'криминал',
    16: 'мелодрама',
    17: 'мистика',
    18: 'музыка',
    19: 'мюзикл',
    20: 'нуар',
    21: 'опера',
    22: 'приключения',
    23: 'семейный',
    24: 'сказка',
    25: 'спектакль',
    26: 'спорт',
    27: 'триллер',
    28: 'ужасы',
    29: 'фантастика',
    30: 'фэнтези'
}

genres = {
    "Анимация": 3006715,
    "аниме": 8164576,
    "балет": 8164576,
    "биография": 3006718,
    "боевик": 3006719,
    "вестерн": 3006720,
    "военный": 3006721,
    "детектив": 8116811,
    "детский": 3006723,
    "документальный": 3006724,
    "драма": 3006725,
    "исторический": 3006726,
    "комедия": 3006727,
    "концерт": 8164577,
    "короткометражный": 3006729,
    "криминал": 3006722,
    "мелодрама": 3006731,
    "мистика": 3006732,
    "музыка": 8164581,
    "мюзикл": 3006734,
    "нуар": 3006735,
    "опера": 8111421,
    "приключения": 3006736,
    "семейный": 3006740,
    "сказка": 3006741,
    "спектакль": 8159033,
    "спорт": 3006742,
    "триллер": 3006744,
    "ужасы": 3006745,
    "фантастика": 3006746,
    "фэнтези": 3006747
}


PARAMS = {}

print("Введите дату, когда хотите сходить в кино в формате YYYY-MM-DD, пустая строка для просмотра фильмов на сегодня")
while True:
    date = input()
    if date != "":
        try:
            datetime.datetime.strptime(date, "%Y-%m-%d")
        except:
            print("Неправильный формат!")
        else:
            PARAMS["date"] = date
            break
    else:
        break

print("Введите жанр фильма(номер) Пустая строка, если Вам не важно")
while True:
    for i, key in enumerate(genres.keys()):
        print(f"{i}: '{key}',")
    number = input()
    if number == "":
        break
    else:
        number = int(number)
    if number < 0 or number > 30:
        print("Нет такого номера!")
    else:
        genre = genres[genres_list[number]]
        PARAMS["genre"] = genre
        break


print("Введите формат: 2D, 2d_dolby_atmos, 3D, HFR, SUB. Пустая строка, если Вам не важно")
while True:
    format = input()
    if format == "":
        break
    if format not in "2D, 2d_dolby_atmos, 3D, HFR, SUB".split(", "):
        print("Нет такого формата!")
    else:
        PARAMS["format"] = format
        break

print("Введите желаемую цену: <200, 200-500, 500-1000, 1000-2000, >2000, пустая строка, если деньги не считаете")
while True:
    price = input()
    if price == "":
        break
    if price not in "<200, 200-500, 500-1000, 1000-2000, >2000".split(", "):
        print("Нет такого диапазона!")
    else:
        PARAMS["price"] = price
        break


key = input(
    "Input the key word:\n'all' or nothing - the list of all films from this page will be printed\n" +
    "'best' - the list of films with the highest raiting (>=9)\n'year' - get films by year\n" +
    "'worst' - the list of films with the lowest raiting (<5)\n'country' - get films released in the particular country\n"
)


URL = "https://msk.kinoafisha.info/movies/"
print("Введите название файла, куда будем выкачивать файл html")
FILE_PATH = input()
print("Введите название файла, куда будем парсить json файл")
PARSED_FILE_PATH = input()

process(URL, FILE_PATH, PARSED_FILE_PATH)

    