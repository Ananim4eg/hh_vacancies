from abc import ABC, abstractmethod  # pragma: no cover
from typing import Any

from src.vacancy import Vacancy


class ApiHH(ABC):  # pragma: no cover
    """Базовый класс, для подключения к api HeadHunters"""

    @abstractmethod
    def _connect_to_api(self) -> bool:
        ...

    @abstractmethod
    def get_vacancies(self, name_vacancy: str) -> str | list:
        ...


class AbsVacancyIO(ABC):  # pragma: no cover
    """Базовый клас для взаимодействия с файлом, который должен хранить список вакансий"""

    @property
    @abstractmethod
    def file_reader(self) -> Any:
        ...

    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy) -> None | str:
        ...

    @abstractmethod
    def delete_vacancy(self, vacancy: Vacancy) -> None | str:
        ...
