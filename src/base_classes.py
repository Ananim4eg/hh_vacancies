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
    def file_worker(self):
        ...


    @file_worker.setter
    @abstractmethod
    def file_worker(self, vacancy):
        ...


    @file_worker.deleter
    @abstractmethod
    def file_worker(self):
        ...