from typing import Any


def get_top_vacancies_by_salary(list_vacancies: list[dict[str, Any]], top_n: int) -> list[dict[str, Any]]:
    """Получение топ вакансий из списка"""

    if not list_vacancies:
        return []

    sort_list = sorted(list_vacancies, key=lambda x: x['salary']['from'], reverse=True)

    return sort_list[:top_n]


def filter_vacancies(list_vacancies: list[dict[str, Any]], key_word: str) -> list[dict[str, Any]]:
    """Фильтрация списка вакансий по ключевым словам"""

    if not list_vacancies:
        return []

    words = key_word.split(', ')

    result_list = []

    for item in list_vacancies:

        if item['snippet']['responsibility']:
            if any(word in item['snippet']['responsibility'] for word in words):  # поверка, что хотя бы 1 из ключевых слов есть в описании вакансии
                preparing_vacancy = {
                    'id вакансии': item['id'],
                    'название вакансии': item['name'],
                    'зарплата от': item['salary']['from'] if type(item['salary']) == dict else "Не указано",  # проверка, что поля не пустые
                    'описание': item['snippet']['responsibility']
                }
                result_list.append(preparing_vacancy)

        else:
            continue

    return result_list
