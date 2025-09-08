import json
import os
from typing import Any

from src.base_classes import AbsVacancyIO
from src.vacancy import Vacancy


class VacancyJSON(AbsVacancyIO):
    """Получает, записывает и удаляет информацию о вакансиях из файла"""

    def __init__(self, file_name: str = 'vacancies.json'):
        self.__file_name = file_name
        self.__file_path = os.path.join(os.path.dirname(__file__), '..', 'data', file_name)

        try:
            with open(self.__file_path, 'w', encoding='utf-8') as file:
                json.dump([], file, indent=4)
        except FileNotFoundError:
            print('Ошибка при создании файла')

    @property
    def file_reader(self) -> Any:
        """Получает информацию о вакансиях из файла json"""

        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                result = json.load(file)
        except FileNotFoundError:
            return f'При чтении файла произошла ошибка. Файл по пути {self.__file_path} не найдет'

        return result

    def add_vacancy(self, vacancy: Vacancy) -> None | str:
        """Добавляет вакансию в файл json"""
        vacancy_info = {
            'имя вакансии': vacancy.name,
            'зарплата': vacancy.salary,
            'ссылка на вакансию': vacancy.vacancy_url,
            'имя компании': vacancy.employer_name,
            'требования': vacancy.requirement
        }

        data = self.file_reader

        if vacancy_info not in data:
            data.append(vacancy_info)

        try:
            with open(self.__file_path, 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
        except FileNotFoundError:
            return f'При добавлении информации произошла ошибка. Файл по пути {self.__file_path} не найдет'

    def delete_vacancy(self, vacancy: Vacancy) -> None | str:
        """Удаляет вакансию из файла json"""
        vacancy_info = {
            'имя вакансии': vacancy.name,
            'зарплата': vacancy.salary,
            'ссылка на вакансию': vacancy.vacancy_url,
            'имя компании': vacancy.employer_name,
            'требования': vacancy.requirement
        }

        data: list[dict[str, Any]] = self.file_reader

        if vacancy_info in data:
            data.remove(vacancy_info)

        try:
            with open(self.__file_path, 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
        except FileNotFoundError:
            return f'При удалении информации произошла ошибка. Файл по пути {self.__file_path} не найдет'
