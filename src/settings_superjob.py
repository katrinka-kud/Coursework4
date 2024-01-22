import requests
import os

from dotenv import load_dotenv

load_dotenv()

superjob_api_key = os.getenv("SuperJob_API_KEY")
url_superjob = "https://api.superjob.ru/2.0/vacancies/"


class SuperJobAPI():
    """Получение данных с сайта SuperJob"""

    def __init__(self, keyword):
        """Инициализация класса
        keyword = ключевое слово для поиска вакансий"""
        self.keyword = keyword
        self.parameters = {
            "count": 100,
            "keyword": self.keyword
            "keywords": {
                "srws": 1,
                "skwc": "or",
                "keys": self.keyword
            }
        }
        self.my_headers = {
            "X-Api-App-Id": superjob_api_key
        }

    def get_vacancies(self, page=0) -> list[dict]:
        """Получение вакансий
        :return: Список с вакансиями"""
        self.parameters["page"] = page
        response = requests.get(url=url_superjob, params=self.parameters, headers=self.my_headers)
        return response.json()["objects"]


# superjob_api = SuperJobAPI('python')
# print(superjob_api.get_vacancies(10))
