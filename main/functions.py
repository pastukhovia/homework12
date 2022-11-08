import json
import logging


def load_posts():
    '''
            Загрузка списка постов из json файла
            args:
            returns: список из постов
            '''

    with open('posts.json', encoding='utf-8') as file:
        file_content = json.loads(file.read())
    return file_content


def get_search_results(query):
    '''
            Получение результатов поискового запроса
            args: query - поисковой запрос
            returns: result - список найденных записей в случае удачи
                     False - в случае, если ничего не найдено
            '''

    result = []
    posts = load_posts()

    for item in posts:
        if query.lower() in item['content'].lower():
            result.append(item)

    if result:
        return result
    else:
        return False


def set_search_logger():
    '''
            Создание логера поисковых запросов
            args:
            returns: объект логгер
            '''

    logger = logging.getLogger('search_logger')
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s : %(message)s")
    file_handler = logging.FileHandler('./search_log.txt', encoding='utf-8')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.info('Начало записи')

    return logger
