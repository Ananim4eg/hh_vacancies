import pytest

from src.vacancy import Vacancy


@pytest.fixture()
def create_vacancy_one():
    return Vacancy(
    "Тестировщик комфорта квартир",
    {
      "from": 350000,
      "to": 450000,
      "currency": "RUR",
      "gross": False
    },
    "https://hh.ru/vacancy/93353083",
    "Специализированный застройщик BM GROUP",
    "Занимать активную жизненную позицию, уметь активно танцевать и громко петь. Обладать навыками коммуникации, чтобы налаживать добрососедские отношения. Обладать системным мышлением..."
)



@pytest.fixture()
def create_vacancy_two():
    return Vacancy(
        "Бортпроводник",
        None,
        "https://hh.ru/vacancy/93209001",
        "«MY FREIGHTER» LLC",
        "Образование: среднее полное (11 классов), среднее специальное, высшее. Обязательное владение узбекским, русским и английским языками. Готовность работать согласно графику полетов."
)



@pytest.fixture()
def create_vacancy_three():
    return Vacancy(
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