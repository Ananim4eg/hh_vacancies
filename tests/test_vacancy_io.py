import json
import os

from src.vacancy_io import VacancyJSON


def test_add_new_vacancy_to_file(create_vacancy_one):
    test_file = VacancyJSON('test.json')

    test_file.add_vacancy(create_vacancy_one)

    with open(os.path.join(os.path.dirname(__file__), '..', 'data', 'test.json') , 'r', encoding='utf-8') as file:
        loaded_data = json.load(file)

    assert loaded_data == [
        {
         'имя вакансии': 'Тестировщик комфорта квартир',
         'зарплата': {
             'from': 350000,
             'to': 450000,
             'currency': 'RUR',
             'gross': False
         },
         'ссылка на вакансию': 'https://hh.ru/vacancy/93353083',
         'имя компании': 'Специализированный застройщик BM GROUP',
         'требования': 'Занимать активную жизненную позицию, уметь активно танцевать и громко петь. '
                       'Обладать навыками коммуникации, чтобы налаживать добрососедские отношения. Обладать '
                       'системным мышлением...'
        }
    ]

    os.remove(os.path.join(os.path.dirname(__file__), '..', 'data', 'test.json'))


def test_remove_vacancy_from_file(create_vacancy_one, create_vacancy_two):
    test_file = VacancyJSON('test.json')

    test_file.add_vacancy(create_vacancy_one)
    test_file.add_vacancy(create_vacancy_two)

    test_file.delete_vacancy(create_vacancy_two)

    with open(os.path.join(os.path.dirname(__file__), '..', 'data', 'test.json') , 'r', encoding='utf-8') as file:
        loaded_data = json.load(file)

    assert loaded_data == [
        {
         'имя вакансии': 'Тестировщик комфорта квартир',
         'зарплата': {
             'from': 350000,
             'to': 450000,
             'currency': 'RUR',
             'gross': False
         },
         'ссылка на вакансию': 'https://hh.ru/vacancy/93353083',
         'имя компании': 'Специализированный застройщик BM GROUP',
         'требования': 'Занимать активную жизненную позицию, уметь активно танцевать и громко петь. '
                       'Обладать навыками коммуникации, чтобы налаживать добрососедские отношения. Обладать '
                       'системным мышлением...'
        }
    ]

    os.remove(os.path.join(os.path.dirname(__file__), '..', 'data', 'test.json'))
