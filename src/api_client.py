from datetime import datetime

import requests

from src.base_classes import ApiHH


class HeadHunterAPI(ApiHH):

    def __init__(self):
        ...


    def __connect_to_api(self):
        """Проверяет доступность api сервиса"""

        url = "https://api.hh.ru/vacancies"

        response = requests.get(url)

        if response.status_code == 200:
            return True

        else:
            return False



    def get_vacancies(self, name_vacancy: str = True, host: str = "hh.ru", pages: int = 0):
        """Получает список вакансий по заданному имени"""

        if not self.__connect_to_api():
            return "Ошибка при подключении к сервису"

        page = pages
        result = []
        while page < 20:
            date_today = datetime.today()
            date = date_today.strftime("%Y-%m-%d")

            url = "https://api.hh.ru/vacancies"

            params = {
                "text": f'!"{name_vacancy}"',
                "search_field": 'name',
                "date_from": date,
                "per_page": 100,
                "page": page
            }

            response = requests.get(url, params=params)
            vacancies = response.json()

            if vacancies.get("items"):
                result.extend(vacancies.get("items"))
            else:
                page += 1
                continue

            page += 1

        if not result:
            return "Подходящих вакансий не найдено"

        unique_vacancies = {vacancy['id']: vacancy for vacancy in result}.values()

        return unique_vacancies
