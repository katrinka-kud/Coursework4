from abc import ABC, abstractmethod
from src.vacancies import Vacancy
import json


class Get_Vacancies(ABC):
    """Абстрактный класс для получения вакансий"""

    def __init__(self, path: str):
        self.path = path

    @abstractmethod
    def get_vacancies(self, vacancies) -> None:
        pass


class Get_JSONSaver(Get_Vacancies):
    """Отбирает и записывает вакансии в файл json"""

    def get_vacancies(self, vacancies):
        all_vacancies = [vacancy.__dict__ for vacancy in vacancies]
        with open(self.path, 'w', encoding='utf-8') as file:
            json.dump(all_vacancies, file, indent=4, ensure_ascii=False)
