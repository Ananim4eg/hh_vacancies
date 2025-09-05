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
        if any(word in item['snippet']['responsibility'] for word in words):  # поверка, что хотя бы 1 из ключевых слов есть в описании вакансии
            result_list.append(item)

    return result_list
