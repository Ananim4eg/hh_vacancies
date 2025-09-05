from src.api_client import HeadHunterAPI
from src.utils import filter_vacancies, get_top_vacancies_by_salary
from src.vacancy import Vacancy
from src.vacancy_io import VacancyJSON


def main():
    print("Приветствую!")

    search_vacancies = input('Введите название вакансии. \nВвод: ')
    hh_api = HeadHunterAPI()
    vacancies_from_hh = hh_api.get_vacancies(search_vacancies)

    if vacancies_from_hh == 'Подходящих вакансий не найдено':
        print('Подходящих вакансий не найдено')

    elif vacancies_from_hh == 'Ошибка при подключении к сервису':
        print('Ошибка при подключении к сервису')

    else:
        separated_vacancies = [Vacancy.add_new_vacancy(vacancy) for vacancy in vacancies_from_hh]

        file_name = input('Введите название файла. \nВвод: ')

        if file_name[-5:] != '.json':
            file_name = file_name + '.json'

        json_save = VacancyJSON(file_name)

        for vacancy in separated_vacancies:
            json_save.add_vacancy(vacancy)
        print(f'Вакансии сохранены в файл {file_name}')

        while True:
            query_for_filtering = input('Нужно отфильтровать данные? Да\Нет \nВвод: ').lower()

            if query_for_filtering not in ['да','нет']:
                continue

            else:
                break

        if query_for_filtering == 'нет':
            return 'Завершение работы'

        else:
            filter_words = input("Введите слова \ связку слов, через запятую, для поиска вакансий \nВвод: ")
            filter_list_vacancies = filter_vacancies(vacancies_from_hh, filter_words)

            if not filter_list_vacancies:
                return 'Таких вакансий не найдено'

            for elem in filter_list_vacancies:
                print(elem)

            top_salary = int(input('Введите число для вывода топ N вакансий по З\П \nВвод: '))

            for elem in get_top_vacancies_by_salary(filter_list_vacancies,top_salary):
                print(elem)


if __name__ == '__main__':
    main()
