from src.api_client import HeadHunterAPI


def main():
    print("Приветствую!")

    search_vacancies = input('Введите название вакансии. \nВвод: ')
    hh_api = HeadHunterAPI()
    vacancies_from_hh = hh_api.get_vacancies(search_vacancies)



if __name__ == '__main__':
    main()