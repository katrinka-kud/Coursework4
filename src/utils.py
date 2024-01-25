from platform import platform

from src.settings_hh import HeadHunterAPI
from src.settings_superjob import SuperJobAPI
from src.vacancies import Vacancy, Vacancy_HeadHunter, Vacancy_SuperJob


def get_vacancy_hh(vacancies: list[dict]):
    """Все найденные вакансии с HeadHunter
    записали в переменную с полями: заголовок вакансии,
                                    город,
                                    заработанная плата от/до,
                                    должностные обязанности,
                                    ссылка на вакансию"""

    list_vacancies = []
    for vacancy in vacancies:
        sample_vacancy = Vacancy_HeadHunter(
            vacancy_title=vacancy['name'],
            vacancy_city=vacancy['address'],
            salary_from=vacancy['salary']['from'],
            salary_to=vacancy['salary']['to'],
            vacancy_responsibilities=vacancy['responsibility'],
            vacancy_url=vacancy['alternate_url']
        )
        list_vacancies.append(sample_vacancy)
    return list_vacancies


def get_vacancy_sj(vacancies: list[dict]):
    """Все найденные вакансии с SuperJob
    записали в переменную с полями: заголовок вакансии,
                                    город,
                                    заработанная плата от/до,
                                    должностные обязанности,
                                    ссылка на вакансию"""

    list_vacancies = []
    for vacancy in vacancies:
        sample_vacancy = Vacancy_SuperJob(
            vacancy_title=vacancy['name'],
            vacancy_city=vacancy['address'],
            salary_from=vacancy['salary']['from'],
            salary_to=vacancy['salary']['to'],
            vacancy_responsibilities=vacancy['responsibility'],
            vacancy_url=vacancy['alternate_url']
        )
        list_vacancies.append(sample_vacancy)
    return list_vacancies


def platform_selection():
    """Позволяет выбрать платформу для поиска вакансии"""
    while True:
        platform = ''
        platform_option = int(input('Выберите платформу для поиска вакансий:\n'
                                    '0 - Затрудняюсь ответить\n'
                                    '1 - HeadHunter\n'
                                    '2 - SuperJob'
                                    'Введите цифру: '))
        if platform_option == '0':
            platform = None
            break
        elif platform_option == '1':
            platform = 'HeadHunter'
            break
        elif platform_option == '2':
            platform = 'SuperJob'
            break
        else:
            print('Вы ввели неверное значение')
            continue
    return platform


def filtered_vacancies_by_salary(vacancies: list[Vacancy], minimal_salary=0):
    """Фильтрует вакансии по минимальной заработанной плате, установленной пользователем"""
    filtered_vacancies = []
    for vacancy in vacancies:
        if vacancy.salary_from >= minimal_salary and vacancy.vacancy_currency == 'RUB':
            filtered_vacancies.append(vacancy)
    return sorted(filtered_vacancies)


def filtered_salary():
    """Фильтрует, введенную пользователем, минимальную заработанную плату"""
    while True:
        salary = 0
        salary_query = input('Введите минимальную заработанную плату: ')
        if not salary_query.isdigit():
            print('Введите целое число')
            continue
        elif int(salary_query) < 0:
            print('Введите целое число')
            continue
        else:
            salary = salary_query
            break
    return int(salary)


def filtered_platform(vacancies, platform):
    """Фильтрует вакансии в выбранной платформе"""
    filtered_vacancies = []
    if platform:
        for vacancy in vacancies:
            if vacancy.platform == platform:
                filtered_vacancies.append(vacancy)
    else:
        filtered_vacancies = vacancies
    return filtered_vacancies


def shows_vacancies(vacancies):
    """Показывает вакансии пользователю"""
    while True:
        top_n = int(input("Введите количество вакансий для вывода в топ N: "))
        if not top_n.isdigit():
            print("Введите целое число")
            continue
        else:
            break
    print("Мы подобрали для Вас вакансии:\n")
    for vacancy in vacancies[0:top_n]:
        if vacancy.vacancy_skills:
            skills = vacancy.vacancy_skills.split('.')
        if vacancy.salary_to > 0:
            print(f'Вакансия: {vacancy.vacancy_name}\n'
                  f'Заработанная плата: {vacancy.vacancy.salary_from - vacancy.vacancy.salary_to}\n'
                  f'Город: {vacancy.vacancy_city}\n'
                  f'Описание: {vacancy.vacancy_responsibilities}\n'
                  f'Ссылка на вакансию: {vacancy.vacancy_url}\n')
        else:
            print(f'Вакансия: {vacancy.vacancy_name}\n'
                  f'Заработанная плата от: {vacancy.vacancy.salary_from}\n'
                  f'Город: {vacancy.vacancy_city}\n'
                  f'Описание: {vacancy.vacancy_responsibilities}\n'
                  f'Ссылка на вакансию: {vacancy.vacancy_url}\n')
