class Vacancy:
    """Собирает данные о вакансиях с разных источников"""

    def __init__(self,
                 vacancy_title: str,
                 vacancy_region: str,
                 salary_from: int,
                 salary_to: int,
                 vacancy_responsibilities: str,
                 vacancy_url: str
                 ):
        self.vacancy_title = vacancy_title  # заголовок вакансии
        self.vacancy_region = vacancy_region  # регион
        self.salary_from = salary_from  # заработанная плата от
        self.salary_to = salary_to  # заработанная плата до
        self.vacancy_responsibilities = vacancy_responsibilities  # должностные обязанности
        self.vacancy_url = vacancy_url  # ссылка на вакансию

    def to_dict(self):
        """Возвращает вакансию в виде словаря"""
        return {"vacancy_title": self.vacancy_title,
                "vacancy_region": self.vacancy_region,
                "salary_from": self.salary_from,
                "salary_to": self.salary_to,
                "vacancy_responsibilities": self.vacancy_responsibilities,
                "vacancy_url": self.vacancy_url}

    def __lt__(self, other):
        if not isinstance(other, Vacancy):
            raise TypeError()
        return self.salary_from < other.salary_from

    def __gt__(self, other):
        if not isinstance(other, Vacancy):
            raise TypeError()
        return self.salary_from > other.salary_from

    def __eq__(self, other):
        if not isinstance(other, Vacancy):
            raise TypeError()
        return self.salary_from == other.salary_from

    def __ne__(self, other):
        if not isinstance(other, Vacancy):
            raise TypeError()
        return self.salary_from != other.salary_from

    def __le__(self, other):
        if not isinstance(other, Vacancy):
            raise TypeError()
        return self.salary_from <= other.salary_from

    def __ge__(self, other):
        if not isinstance(other, Vacancy):
            raise TypeError()
        return self.salary_from >= other.salary_from


class Vacancy_HeadHunter(Vacancy):
    """Класс, указывающий с какой платформы вакансия"""

    def __init__(self,
                 vacancy_title: str,
                 vacancy_region: str,
                 salary_from: int,
                 salary_to: int,
                 vacancy_responsibilities: str,
                 vacancy_url: str
                 ):
        super().__init__(vacancy_title,
                         vacancy_region,
                         salary_from,
                         salary_to,
                         vacancy_responsibilities,
                         vacancy_url)
        self.platfom = "HeadHunter"

    def __str__(self):
        return f"Вакансия с HeadHunter: {self.vacancy_title}"

    def to_json(self):
        vacancy = super().to_json()
        vacancy['platfom'] = 'HeadHunter'
        return vacancy


class Vacancy_SuperJob(Vacancy):
    """Класс, указывающий с какой платформы вакансия"""

    def __init__(self,
                 vacancy_title: str,
                 vacancy_region: str,
                 salary_from: int,
                 salary_to: int,
                 vacancy_responsibilities: str,
                 vacancy_url: str
                 ):
        super().__init__(vacancy_title,
                         vacancy_region,
                         salary_from,
                         salary_to,
                         vacancy_responsibilities,
                         vacancy_url)
        self.platfom = "SuperJob"

    def __str__(self):
        return f"Вакансия с SuperJob: {self.vacancy_title}"

    def to_json(self):
        vacancy = super().to_json()
        vacancy['platfom'] = 'SuperJob'
        return vacancy
