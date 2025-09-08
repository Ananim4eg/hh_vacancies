from src.vacancy import Vacancy


def test_vacancy_init(create_vacancy_one):
    vacancy = create_vacancy_one

    assert vacancy.name == "Тестировщик комфорта квартир"
    assert vacancy.salary == {
      "from": 350000,
      "to": 450000,
      "currency": "RUR",
      "gross": False
    }
    assert vacancy.vacancy_url == "https://hh.ru/vacancy/93353083"
    assert vacancy.employer_name == "Специализированный застройщик BM GROUP"
    assert vacancy.requirement == (
        "Занимать активную жизненную позицию, уметь активно танцевать и громко петь. Обладать "
        "навыками коммуникации, чтобы налаживать добрососедские отношения. Обладать системным мышлением..."
    )


def test_vacancy_init_no_salary(create_vacancy_two):
    vacancy = create_vacancy_two

    assert vacancy.salary == 'Не указано'


def test_comparison_methods(create_vacancy_one, create_vacancy_two, create_vacancy_three):
    vac1 = create_vacancy_one
    vac2 = create_vacancy_two
    vac3 = create_vacancy_three

    assert vac1.__lt__(vac2) == 'В одной или нескольких вакансиях не указана зарплата'
    assert vac1.__lt__(vac3) == False
    assert vac3.__gt__(vac1) == False
    assert vac2.__gt__(vac1) == "В одной или нескольких вакансиях не указана зарплата"
    assert vac3.__lt__(vac1) == True
    assert vac1.__gt__(vac3) == True
    assert vac1.__eq__(vac3) == False
    assert vac2.__eq__(vac3) == "В одной или нескольких вакансиях не указана зарплата"


def test_class_method_created_vacancy():
    vacancy = Vacancy.add_new_vacancy(
        {

            "name": "Бортпроводник",
            "salary": None,
            "alternate_url": "https://hh.ru/vacancy/93209001",
            "employer": {
                "name": "«MY FREIGHTER» LLC",
            },
            "snippet": {
                "requirement": "Образование: среднее полное (11 классов), среднее специальное, высшее. Обязательное "
                               "владение узбекским, русским и английским языками. Готовность работать согласно"
                               " графику полетов. ",
            },
        }
    )

    assert vacancy.name == "Бортпроводник"
    assert vacancy.salary == "Не указано"
    assert vacancy.vacancy_url == "https://hh.ru/vacancy/93209001"
    assert vacancy.employer_name == "«MY FREIGHTER» LLC"
    assert vacancy.requirement == "Образование: среднее полное (11 классов), среднее специальное, высшее. Обязательное\
 владение узбекским, русским и английским языками. Готовность работать согласно графику полетов. "