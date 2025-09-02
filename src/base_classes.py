from abc import ABC, abstractmethod


class ApiHH(ABC):

    @abstractmethod
    def __connect_to_api(self):
        ...


    @abstractmethod
    def get_vacancies(self):
        ...
