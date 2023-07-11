from src.api import HeadHunter, SuperJob
from src.description import Description
from src.saver import JsonSaver


def user_interaction():
    #top_n = input('Введите количество вакансий для вывода в топ:\n')
    hh = HeadHunter()
    sj = SuperJob()
    saver = JsonSaver()

    keyword = input('Введите ключевое слово для поиска вакансий:\n')
    all_vacancies_list = hh.output_info(keyword)
    sj_vacancies_list = sj.output_info(keyword)
    all_vacancies_list.extend(sj_vacancies_list)
    all_vacancies = []
    for vacancy_dict in all_vacancies_list:
        vacancy = Description(**vacancy_dict)
        all_vacancies.append(vacancy)

    filter_with_salary = input('Отфильтровать вакансии только с указанной минимальной зарплатой? (y/n): ')
    if filter_with_salary.lower() == 'y':
        all_vacancies = Description.filter_with_salary(all_vacancies)

    print('Отсортировать вакансии по дате публикации или минимальной зарплате?')
    print('date - по дате, salary - по зарплате, no - не сортировать')
    sort_by = input().lower()
    if sort_by in ['date', 'd']:
        all_vacancies = Description.sort_by_date(all_vacancies)
    elif sort_by in ['salary', 's']:
        all_vacancies = Description.sort_by_salary(all_vacancies)

    saver = JsonSaver()
    saver.add_descriptions(all_vacancies)

    keywords = input('Введите ключевые слова для фильтрации, через пробел:\n')
    if keywords.strip():
        filtered_vacancies_list = saver.get_by_keywords(keywords)
        filtered_vacancies = []
        for vacancy in filtered_vacancies_list:
            filtered_vacancies.append(Description(**vacancy))
    else:
        filtered_vacancies = all_vacancies
    if len(filtered_vacancies) == 0:
        print('По вашему запросу не найдено вакансий')
    else:
        print('Введите количество вакансий из топа для вывода (до 200):')
        top_n = int(input())
        top_n = min(top_n, len(filtered_vacancies))
        for i in range(top_n):
            vacancy = filtered_vacancies[i]
            print(vacancy.name)

            if vacancy.salary['from'] is None:
                if vacancy.salary['to'] is None:
                    print('Зарплата не указана')
                else:
                    print(f'Зарпалата до {vacancy.salary["to"]}')
            elif vacancy.salary['to'] is None:
                print(f'Зарплата от {vacancy.salary["from"]}')
            else:
                print(f'Зарплата от {vacancy.salary["from"]} до {vacancy.salary["to"]}')

            print('Описание:\n')
            print(vacancy.description)
            print(f'Опубликовано {vacancy.date_published}')
            print(vacancy.link)
            print()
            print('-------------')
            print()


if __name__ == '__main__':
    user_interaction()