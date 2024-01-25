from abc import ABC, abstractmethod
from src.vacancies import Vacancy
import json


class Get_Vacancies(ABC):
    """Абстрактный класс для получения вакансий"""

    def __init__(self, path):
        self.path = path

    @abstractmethod
    def get_vacancies(self, vacancies) -> None:
        pass


class Get_JSONSaver(Get_Vacancies):
    """Отбирает и записывает вакансии в файл json"""

    @staticmethod
    def sorting_salaries_rub(vacancies: list[Vacancy]):
        sorted_vacancies = []
        for vacancy in vacancies:
            if vacancy.vacancy_currency == 'RUB':
                sorted_vacancies.append(vacancy)
        return sorted_vacancies

    def add_vacancy(self, vacancies):
        all_vacancies = [vacancy.to_json() for vacancy in self.sorting_salaries_rub(vacancies)]
        with open(self.path, 'w', encoding='utf-8') as file:
            json.dump(all_vacancies, file, indent=2, ensure_ascii=False)
