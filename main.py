from src.settings_hh import HeadHunterAPI
from src.settings_superjob import SuperJobAPI
from src.abstract_class import *
from src.utils import *


def main():
    search_word = input("Введите поисковый запрос:\n")
    platform = platform_selection()
    minimal_salary = filtered_salary()

    hh_api = HeadHunterAPI(search_word)
    sj_api = SuperJobAPI(search_word)

    hh_vacancies = get_vacancy_hh(hh_api.get_vacancies)
    sj_vacancies = get_vacancy_sj(sj_api.get_vacancies)

    filtered_vacancies_salary = filtered_vacancies_minimal_salary(hh_vacancies + sj_vacancies, minimal_salary)
    top_vacancies = filtered_platform(hh_vacancies + sj_vacancies, platform)
    if len(top_vacancies) == 0:
        print("Нет вакансий, соответствующих заданным критериям.")
    else:
        print(f'Мы нашли для Вас {len(top_vacancies)} вакансий')
        shows_vacancies(top_vacancies)

    json_saver = Get_JSONSaver('vacancies.json')
    json_saver.get_vacancies(hh_vacancies + sj_vacancies)


if __name__ == '__main__':
    main()
