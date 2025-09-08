from src.utils import filter_vacancies, get_top_vacancies_by_salary


def test_filter_by_key_words():
    data = [
        {
        'id':0,
        'name': 0,
        'salary': {
            'from':0
        },
        'snippet': {
            'requirement': 'пример слов для поиска - карандаш, мел, парта'
        }
    },{
        'id':0,
        'name': 0,
        'salary': {
            'from':0
        },
        'snippet': {
            'requirement': 'пример слов для поиска - газон, мяч, ворота'
        }
    },{
        'id':0,
        'name': 0,
        'salary': {
            'from':0
        },
        'snippet': {
            'requirement': 'пример слов для поиска - кино, попкорн, билет'
        }
    },{
        'id':0,
        'name': 0,
        'salary': {
            'from':0
        },
        'snippet': {
            'requirement': 'пример слов для поиска - карандаш, мяч, билет'
        }
    },{
        'id':0,
        'name': 0,
        'salary': {
            'from':0
        },
        'snippet': {
            'requirement': 'пример слов для поиска - газон, попкорн, ворота'
        }
    }
    ]

    assert filter_vacancies(data, 'кино, парта') == [
        {
         'id вакансии': 0,
         'название вакансии': 0,
         'зарплата от': 0,
         'описание': 'пример слов для поиска - карандаш, мел, парта'
        },
        {
         'id вакансии': 0,
         'название вакансии': 0,
         'зарплата от': 0,
         'описание': 'пример слов для поиска - кино, попкорн, билет'
        }
    ]
    assert filter_vacancies([],'') == []


def test_get_top_vacancies():
    data = [
        {
            'зарплата от': 6
        },
        {
            'зарплата от': 4
        },
        {
            'зарплата от': 2
        },
        {
            'зарплата от': 10
        },
        {
            'зарплата от': 8
        },
    ]


    assert get_top_vacancies_by_salary(data, 4) == [
        {
            'зарплата от': 10
        },
        {
            'зарплата от': 8
        },
        {
            'зарплата от': 6
        },
        {
            'зарплата от': 4
        },
    ]

    assert get_top_vacancies_by_salary([], 3) == []