import os

from src.base_classes import AbsVacancyIO


PATH_TO_FILE = os.path.join(os.path.dirname(__file__), '..', 'data')


class VacancyJSON(AbsVacancyIO):
    """Получает, записывает и удаляет информацию о вакансиях из файла"""

    def __init__(self, file_name: str = 'vacancies.json'):
        self.__file_name = file_name
        self.__file_path = os.path.join(os.path.dirname(__file__), '..', 'data', file_name)


    @property
    def file_worker(self):
        return None


    @file_worker.setter
    def file_worker(self, vacancy):
        ...


    @file_worker.deleter
    def file_worker(self):
        ...


