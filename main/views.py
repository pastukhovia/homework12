import logging
from datetime import datetime
from json import JSONDecodeError
from flask import render_template, Blueprint, request
from main.functions import get_search_results, set_search_logger

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='./templates')

search_logger = set_search_logger()


@main_blueprint.route('/')
def main_page():
    return render_template('index.html')


@main_blueprint.route('/search')
def search_page():
    query = request.args.get('s')

    try:
        result = get_search_results(query)
    except FileNotFoundError:
        logging.error(f'{datetime.datetime.now()}: Файл не найден')
        return 'Файл не найден.'
    except JSONDecodeError:
        return 'Ошибка чтения файла JSON'

    search_logger.info(f'Поисковой запрос: {query}')

    return render_template('post_list.html', items=result, query=query)
