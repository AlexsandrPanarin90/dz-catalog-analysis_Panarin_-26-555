import math

movies = [
    {"title": "The Dune Chronicles", "year": 2021,
     "genres": {"sci-fi", "drama"}, "rating": 8.6,
     "duration_min": 155, "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019,
     "genres": {"comedy", "drama"}, "rating": 7.1,
     "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016,
     "genres": {"thriller", "drama"}, "rating": 6.4,
     "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023,
     "genres": {"sci-fi", "action"}, "rating": 5.9,
     "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014,
     "genres": {"comedy"}, "rating": 7.8,
     "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020,
     "genres": {"thriller", "mystery"}, "rating": 8.9,
     "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022,
     "genres": {"drama"}, "rating": 4.8,
     "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024,
     "genres": {"sci-fi", "drama"}, "rating": 9.2,
     "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011,
     "genres": {"comedy"}, "rating": 6.0,
     "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018,
     "genres": {"action", "thriller"}, "rating": 7.3,
     "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]

# Этап 1. Разминка: переменные, числа, math
def average_rating(movies):
    """Возвращает среднюю оценку по каталогу"""
    if not movies:
        return 0.0
    total = sum(movie["rating"] for movie in movies)
    return round(total / len(movies), 1)


def catalog_age_stats(movies, current_year=2026):
    """Возвращает кортеж (самый старый, самый новый, среднее)."""
    if not movies:
        return (0, 0, 0)
    ages = [current_year - movie["year"] for movie in movies]
    av = math.ceil(sum(ages) / len(ages))
    old = max(ages)
    new = min(ages)
    return (old, new, av)


def duration_in_hours(minutes):
    """Переводит минуты в формат "2ч 35м"""
    h = minutes // 60
    m = minutes % 60
    return f"{h}ч {m}м"



# Этап 2
# Задача 1. Напишите функцию rating_tier(rating), 
# которая по оценке возвращает категорию: 
# "шедевр" (≥9), "хорошо" (7–8.9), "средне" (5–6.9), "слабо" (<5). 
# Реализуйте ее через if/elif, а внутри используйте 
# тернарный оператор хотя бы один раз.

def rating_tier(rating):
    if rating >= 9:
        # Тернарный оператор: проверяем, не пустой ли рейтинг
        return "слабо" if rating is None else "шедевр"
    elif rating >= 7:
        return "хорошо"
    elif rating >= 5:
        return "средне"
    else:
        return "слабо"


# Задача 2. Напишите функцию rating_tier(rating), 
# которая по оценке возвращает категорию: 
# Напишите функцию decade_label(year), 
# которая через оператор match 
# возвращает метку "новые" (после 2020), 
# "недавние" (2015–2020) или "старые" (раньше 2015).
def decade_label(year):
  match year:
    case year if year>2020:
      return "новые"
    case year if year<=2020 and year>=2015 :
      return "недавние"
    case year if year<2015:  
      return "старые" 


# Этап 3. Циклы
# Продемонстрируйте работу с for, while и управляющими 
# конструкциями циклов на каталоге.
# С помощью for и continue выведите на экран (print) названия всех фильмов, 
# которые НЕ относятся к жанру "comedy".
# С помощью while и break найдите первый по порядку 
# в списке фильм с рейтингом выше 9.0; 
# если такого фильма нет, 
# цикл должен завершиться веткой else с сообщением "Шедевров не найдено".
# Напишите функцию count_long_movies(movies, threshold=120), 
# которая через for с накопительной переменной 
# считает количество фильмов длиннее threshold минут.
# Обязательно использовать continue в первом пункте и break — во втором. 
# Ветка else цикла while должна 
# быть по-настоящему задействована (проверьте и случай, когда шедевров нет). 
# В count_long_movies нельзя использовать sum() 
# по списку-фильтру — только накопление в цикле. 
   
#Задача 1
for mov in movies:
  if 'comedy' in mov['genres']:
    continue
  else:
    print(mov['title'])   

#Задача 2
i = 0
while i < len(movies):
    if movies[i]["rating"] > 9.0:
        print(f"Найден: {movies[i]['title']}")
        break 
    i += 1
else:
    print("Шедевров не найдено")

#Задача 3
def count_long_movies(movies, threshold=120):
  i = 0
  for mov in movies:
    if mov['duration_min']> threshold:
      i += 1
  return i    


#Этап 4. Строки
# 1) Напишите функцию normalize_title(title), 
# которая приводит строку к формату Title Case (каждое слово с заглавной буквы) 
# без использования str.title() напрямую: разбейте строку по пробелам 
# и соберите заново вручную, меняя первую букву каждого слова через 
# срез (word[0].upper() + word[1:]).
# 2) Напишите функцию make_slug(title), которая превращает нормализованное 
# название в «слаг» вида the-quiet-algorithm.
# 3) Напишите функцию format_report_line(movie), возвращающую единую 
# строку с описанием фильма. Пример результата
# -- normalize_title("silent hours") # "Silent Hours"
# -- make_slug("Silent Hours") # "silent-hours"
# -- format_report_line(movies[7])
# --  '"The Quiet Algorithm" (2024) — 9.2/10, 1ч 58м, жанры: drama, sci-fi'

# Задача 1
def normalize_title(title):
    words = title.split()
    # в задании нет требования, но я добавил проверку на пустую строку
    if not words:
        return title

    title_up = words[0][0].upper() + words[0][1:]
    for word in words[1:]:
        title_up += " " + word[0].upper() + word[1:]
    return title_up

# Задача 2
def make_slug(title):
    normal = normalize_title(title)
    return normal.lower().replace(" ", "-")

# Задача 3
def format_report_line(movie):
    title = normalize_title(movie["title"])
    genres_str = ", ".join(sorted(movie["genres"]))
    duration = duration_in_hours(movie["duration_min"])
    return (
        f'"{title}" ({movie["year"]}) — {movie["rating"]}/10, '
        f'{duration}, жанры: {genres_str}'
    )



#Этап 5. Списки
#Задача:
#Напишите функцию titles_sorted_by_rating(movies), 
# возвращающую список названий фильмов, отсортированных 
# по убыванию рейтинга. Напишите функцию 
# top_n_by_rating(movies, n=3), возвращающую список из n 
# кортежей (title, rating) — топ по рейтингу.

#Пример результата:
#top_n_by_rating(movies, 3)
#[("The Quiet Algorithm", 9.2), ("midnight in oslo", 8.9), 
#("The Dune Chronicles", 8.6)]
#Требования:
#Сортировку выполнять через sorted() с параметром key, а не 
# вручную через циклы сравнения. Каждая запись в top_n_by_rating — именно tuple, 
# а не список. titles_sorted_by_rating не должна изменять исходный список movies. 
# Подсказка key принимает функцию, которая возвращает значение для сравнения элементов; 
# для сортировки по убыванию пригодится параметр reverse=True.
#

#Задача 1
def titles_sorted_by_rating(movies):
  titles_sort = sorted(movies, key = lambda x: x['rating'], reverse=True)
  titles = [movie["title"] for movie in titles_sort]
  return titles

#Задача 2
def top_n_by_rating(movies, n=3):
  title_sort = sorted(movies, key=lambda x: x['rating'],reverse=True)
  movies_top = title_sort[0:n]
  result = []
  for movie in movies_top:
    result.append((movie['title'], movie['rating'])) 
  return result


#Этап 6. Словари
#Задача
#1) Напишите функцию count_by_genre(movies), 
# возвращающую словарь {жанр: количество фильмов}, 
# построенный вручную через цикл и метод dict.get() (без Counter).
#2) Напишите функцию actor_filmography(movies), возвращающую словарь 
# {актер: [список названий фильмов]}. 
# С помощью генератора словаря (dict comprehension) 
# постройте словарь {title: rating} только для фильмов с рейтингом 
# выше среднего (используйте average_rating из этапа 1).

#Задача 1
def count_by_genre(movies):

  genre_result = {}
  for movie in movies:
    for genre in movie['genres']:
      genre_result[genre] = genre_result.get(genre, 0) + 1
  return genre_result   

#Задача 2
def actor_filmography(movies):
    films = {}
    for movie in movies:
        for actor in movie["actors"]:
            films[actor] = films.get(actor, [])
            films[actor].append(movie["title"])
    return films






# Этап 7. Множества
#Задача
#Напишите функцию all_genres(movies), возвращающую множество 
# всех уникальных жанров каталога.
#Напишите функцию common_actors(movie1, movie2), 
# возвращающую множество актеров, снимавшихся в обоих фильмах.
#Напишите функцию genres_only_in_one(movies_a, movies_b), 
# которая возвращает жанры, встречающиеся в movies_a, 
# но не встречающиеся в movies_b.

#Задача 1
def all_genres(movies):
  #for movie in movies:
  all_genre = set()
  for movie in movies:
    all_genre.update(movie["genres"])
  return all_genre


#Задача 2
def common_actors(movie1, movie2):
  actors_mov = set()
  act_mv1 = set(movie1['actors'])
  act_mv2 = set(movie2['actors'])
  actors_mov = act_mv1 & act_mv2
  return actors_mov

#Задача 3
def genres_only_in_one(movies_a, movies_b):
    genres_a = all_genres(movies_a)
    genres_b = all_genres(movies_b)
    return genres_a - genres_b




#Этап 8. Итераторы и генераторы
# Задача
# Напишите функцию-генератор iter_high_rated(movies, min_rating=8.0),
# которая через yield лениво отдает фильмы с рейтингом не ниже min_rating. 
# Продемонстрируйте ее работу циклом for с вызовом format_report_line. 
# Напишите генераторное выражение, которое считает 
# суммарную длительность всех фильмов с рейтингом выше 7 в минутах, 
# и передайте его в sum().

#Задача 1
def iter_high_rated(movies, min_rating=8.0):
  for movie in movies:
    if movie['rating']>= min_rating:
      yield movie
      
for movie in iter_high_rated(movies):
    print(format_report_line(movie))

#Задача 2
total_duration = sum(film["duration_min"] for film in movies if film["rating"] > 7)
print(total_duration)    

#Этап 9. Итоговый отчет
#Напишите функцию build_report(movies), которая объединяет 
#результаты всех предыдущих этапов в единый консольный отчет: 
#общую статистику, топ-3 фильма, количество фильмов по каждому 
#жанру и полный список уникальных жанров каталога. Пример отчета
#Задача Отчет
def build_report(movies):
    """Собирает и печатает итоговый отчет по каталогу."""
    print("ОТЧЕТ ПО КАТАЛОГУ")

    avg_rating = average_rating(movies)
    print(f"Средний рейтинг: {avg_rating}")

    avg_age = catalog_age_stats(movies)[2]
    print(f"Средний возраст фильмов: {avg_age} лет")
    

    print("\nТоп-3 фильма:")
    top_3 = top_n_by_rating(movies, 3) 

    for title, rating in top_3:
        for movie in movies:
            if movie["title"] == title:
                print(f"  {format_report_line(movie)}")
                break
                
    print("\nФильмов по жанрам:")
    genre_counts = count_by_genre(movies)
    sorted_genres = sorted(
        genre_counts.items(), key=lambda item: item[1], reverse=True
    )
    for genre, count in sorted_genres:
        print(f"  {genre} — {count}")

    print(count_by_genre(movies))

    print("\nВсе жанры каталога:", end=" ")
    genres_set = all_genres(movies)

    genres_sorted = sorted(genres_set)
    print(", ".join(genres_sorted))



if __name__ == "__main__":
    build_report(movies)