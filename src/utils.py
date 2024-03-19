from typing import Any
import requests


def get_hh_data(companies):
    """
    Получает данные о работадателях и вакансиях в формате json
    :return: list[dict[str, Any]]
    """
    data = []
    for company in companies:
        page = 0
        while True:
            company_data = requests.get(f"https://api.hh.ru/vacancies",
                                        params={'employer_id': f'{company}',
                                                'area': 113,
                                                'per_page': 100,
                                                'page': f'{page}'}).json()
            if page >= company_data['pages'] - 1:
                break
            page += 1
        data.append({'company': company_data['items'][0]['employer'],
                    'vacancies': company_data['items'][0]})
    return data


def create_database(database_name, params):
    """
    Создает базу данных и таблицы для сохранения вакансий
    :param database_name: str
    :param params: dict
    :return:
    """
    pass


def save_data_to_database(data, database_name, params):
    """
    Сохраняет данные о вакансиях в базу данных
    :param database_name: list[dict[str, Any]]
    :param data: str
    :param params: dict
    :return:
    """
    cursor = conn.cursor()

    create_table_query = """
        CREATE TABLE IF NOT EXISTS vacancies (
                id SERIAL PRIMARY KEY,
                city VARCHAR(50),
                company VARCHAR(200),
                industry VARCHAR(200),
                title VARCHAR(200),
                keywords TEXT,
                skills TEXT,
                experience VARCHAR(50),
                salary VARCHAR(50),
                url VARCHAR(200)
        )
    """
    cursor.execute(create_table_query)

    conn.commit()
    cursor.close()
    logging.info("Таблица 'vacancies' успешно создана.")
