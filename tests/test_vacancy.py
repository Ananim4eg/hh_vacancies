from src.vacancy import Vacancy
from src.vacancy_io import VacancyJSON

vac1 = Vacancy(
    "Тестировщик комфорта квартир",
    {
      "from": 350000,
      "to": 450000,
      "currency": "RUR",
      "gross": False
    },
    "https://hh.ru/vacancy/93353083",
    "Специализированный застройщик BM GROUP",
    "Занимать активную жизненную позицию, уметь активно танцевать и громко петь. Обладать навыками коммуникации, чтобы налаживать добрососедские отношения. Обладать системным мышлением...")

vac2 = Vacancy(
    "Бортпроводник",
    None,
    "https://hh.ru/vacancy/93209001",
    "«MY FREIGHTER» LLC",
    "Образование: среднее полное (11 классов), среднее специальное, высшее. Обязательное владение узбекским, русским и английским языками. Готовность работать согласно графику полетов. ")

vac3 = Vacancy(
    "Оператор ПК, оператор базы данных",
    {
        "from":160000,
        "to":None,
        "currency":"RUR",
        "gross":True
    },
    "https://hh.ru/vacancy/93166058",
    "Рост Развитие Решение",
    "Опыт в продажах. Опыт работы с клиентами. Умение проводить переговоры. Мобильность."
)


file_one = VacancyJSON()

file_one.add_vacancy(vac3)
file_one.add_vacancy(vac1)

print(file_one.file_reader)

file_one.delete_vacancy(vac1)

print(file_one.file_reader)