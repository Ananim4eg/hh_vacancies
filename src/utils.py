from typing import Any


def get_top_vacancies_by_salary(list_vacancies: list[dict[str, Any]], top_n: int) -> list[dict[str, Any]]:
    """Получение топ вакансий из списка"""

    if not list_vacancies:
        return []

    sort_list = sorted(list_vacancies, key=lambda x: x['зарплата от'], reverse=True)

    return sort_list[:top_n]


def filter_vacancies(list_vacancies: list[dict[str, Any]], key_word: str) -> list[dict[str, Any]]:
    """Фильтрация списка вакансий по ключевым словам"""

    if not list_vacancies:
        return []

    words = key_word.split(', ')

    result_list = []

    for item in list_vacancies:

        if item['snippet']['requirement']:
            # поверка, что хотя бы 1 из ключевых слов есть в описании вакансии
            if any(word in item['snippet']['requirement'] for word in words):
                preparing_vacancy = {
                    'id вакансии': item['id'],
                    'название вакансии': item['name'],
                    # проверка, что поля не пустые
                    'зарплата от': item['salary']['from'] if type(item['salary']) is dict else 0,
                    'описание': item['snippet']['requirement']
                }
                result_list.append(preparing_vacancy)

        else:
            continue

    return result_list
