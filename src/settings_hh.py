import requests

url_hh = "https://api.hh.ru/vacancies"


class HeadHunterAPI():
    """Получение данных с сайта HeadHunter"""

    def __init__(self, keyword: str):
        """Инициализация класса
        keyword = ключевое слово для поиска вакансий"""
        self.keyword = keyword
        self.parameters = {
            "per_page": 100,
            "text": self.keyword,
            "search_field": "name",
            "page": 0
        }

    def get_vacancies(self) -> list[dict]:
        """Получение вакансий
        :return: Список с вакансиями"""
        response = requests.get(url=url_hh, params=parameters)
        return response.json()["items"]


# hh_api = HeadHunterAPI('python')
# print(hh_api.get_vacancies)
