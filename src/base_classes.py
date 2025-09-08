from abc import ABC, abstractmethod  # pragma: no cover


class ApiHH(ABC):  # pragma: no cover
    """Базовый класс, для подключения к api HeadHunters"""

    @abstractmethod
    def _connect_to_api(self):
        ...


    @abstractmethod
    def get_vacancies(self):
        ...


class AbsVacancyIO(ABC): # pragma: no cover
    """Базовый клас для взаимодействия с файлом, который должен хранить список вакансий"""

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