from typing import Any


class Vacancy:
    """Класс для работы с отдельными вакансиями. Сравнение вакансий."""

    __slots__ = ("name", "salary", "vacancy_url", "employer_name", "requirement")


    def __init__(self, name: str, salary: dict[str, Any]|None, vacancy_url: str, employer_name: str, requirement: str):
        self.name = name
        self.__validation_salary(salary)
        self.vacancy_url = vacancy_url
        self.employer_name = employer_name
        self.requirement = requirement


    def __lt__(self, other):
        if self.__check_type_attribute(other):
            if self.salary.get('from') < other.salary.get('from'):
                return True
            return False
        else:
            return "В одной или нескольких вакансиях не указана зарплата"


    def __gt__(self, other):
        if self.__check_type_attribute(other):
            if self.salary.get('from') > other.salary.get('from'):
                return True
            return False
        else:
            return "В одной или нескольких вакансиях не указана зарплата"


    def __eq__(self, other):
        if self.__check_type_attribute(other):
            if self.salary.get('from') == other.salary.get('from'):
                return True
            return False
        else:
            return "В одной или нескольких вакансиях не указана зарплата"


    def __validation_salary(self, salary: dict[str, Any]|None):
        """Валидация данных в графе salary"""

        self.salary = salary

        if not salary:
            self.salary = "Не указано"
        else:
            if not salary.get('from'):
                self.salary['from'] = "Не указано"



    def __check_type_attribute(self, other):
        """Проверка типов данных перед сравнением цен у объектов"""

        if type(self.salary) == str or type(other.salary) == str:
            return False
        elif type(self.salary.get('from')) == str or type(other.salary.get('from')) == str:
            return False
        else:
            return True


    @classmethod
    def add_new_vacancy(cls, vacancy: dict[str, Any]):
        """Создает объект класса Vacancy"""

        return cls(
            vacancy['name'],
            vacancy['salary'],
            vacancy['alternate_url'],
            vacancy['employer']['name'],
            vacancy['snippet']['requirement']
        )

