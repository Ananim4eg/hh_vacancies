from datetime import datetime

import requests

from src.base_classes import ApiHH


class HeadHunterAPI(ApiHH):
    """Получает вакансии с API HeadHunter"""

    def _connect_to_api(self) -> bool:
        """Проверяет доступность api сервиса"""

        url = "https://api.hh.ru/vacancies"

        response = requests.get(url)

        if response.status_code == 200:
            return True

        else:
            return False


    def get_vacancies(self, name_vacancy: str = True, *, host: str = "hh.ru", pages: int = 0) -> str|list[dict]:
        """Получает список вакансий по заданному имени"""

        if not self._connect_to_api():
            return "Ошибка при подключении к сервису"

        page = pages
        result = []

        date_today = datetime.today()
        date = date_today.strftime("%Y-%m-%d")

        url = "https://api.hh.ru/vacancies"

        while page < 20:

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

        unique_vacancies = list({vacancy['id']: vacancy for vacancy in result}.values())  # удаление дубликатов

        return unique_vacancies
