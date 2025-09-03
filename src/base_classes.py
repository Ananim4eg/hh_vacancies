from abc import ABC, abstractmethod


class ApiHH(ABC):


    @abstractmethod
    def _connect_to_api(self):
        ...


    @abstractmethod
    def get_vacancies(self):
        ...


class AbsVacancyIO(ABC):


    @property
    @abstractmethod
    def file_reader(self):
        ...


    @abstractmethod
    def add_vacancy(self, vacancy):
        ...


    @abstractmethod
    def delete_vacancy(self, vacancy):
        ...