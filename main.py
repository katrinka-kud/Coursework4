from settings import VACANCIES_PATH
from src.settings_hh import HeadHunterAPI
from src.settings_superjob import SuperJobAPI
from src.abstract_class import *
from src.utils import *


def main():
    json_file = Get_JSONSaver(VACANCIES_PATH)

    search_query = input("Введите поисковый запрос: ")
    platforms = platform_selection()
    minimal_salary = filtered_salary

    hh_api = HeadHunterAPI(search_query)
    sj_api = SuperJobAPI(search_query)

    hh_vacancies = hh_vacancies_list(hh_api.get_vacancies())
    sj_vacancies = sj_vacancies_list(sj_api.get_vacancies())

    json.file.add_vacancy(hh_vacancies + sj_vacancies)

    sorted_vacancies = filtered_vacancies_by_salary(hh_vacancies + sj_vacancies, minimal_salary)
    top_vacancies = filtered_platform(sorted_vacancies, platform)
    if len(top_vacancies) == 0:
        print("Нет вакансий, соответствующих заданным критериям.")
    else:
        print(f'Мы нашли для Вас {len(top_vacancies)} вакансий')
        shows_vacancies(top_vacancies)


if __name__ == '__main__':
    main()
