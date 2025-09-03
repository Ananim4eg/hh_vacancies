from typing import Any


class VacancyAnalyzer:
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


vac1 = VacancyAnalyzer(
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

vac2 = VacancyAnalyzer(
    "Бортпроводник",
    None,
    "https://hh.ru/vacancy/93209001",
    "«MY FREIGHTER» LLC",
    "Образование: среднее полное (11 классов), среднее специальное, высшее. Обязательное владение узбекским, русским и английским языками. Готовность работать согласно графику полетов. ")

vac3 = VacancyAnalyzer(
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

print(vac3.salary)
