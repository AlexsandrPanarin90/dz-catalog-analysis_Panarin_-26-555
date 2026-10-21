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


