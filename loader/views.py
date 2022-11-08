from json import JSONDecodeError
from flask import render_template, Blueprint, request
from loader.functions import save_post_to_json, set_upload_logger
import logging
import datetime

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

upload_logger = set_upload_logger()
logging.basicConfig(filename='errors.txt', encoding='utf-8')

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='./templates')


@loader_blueprint.route('/upload')
def upload_page():
    return render_template('post_form.html')


@loader_blueprint.route('/upload/saved', methods=['POST'])
def uploaded_page():
    try:
        picture = request.files.get('picture')
        text = request.form.get('content')
        filename = picture.filename

        extension = filename.split(".")[-1]
        if extension in ALLOWED_EXTENSIONS:
            is_saved = save_post_to_json(picture, text)
            return render_template('post_uploaded.html', filename=filename, content=text, is_saved=is_saved)
        else:
            upload_logger.info(f'Попытка загрузить файл формата {extension}')
            return f'Файлы типа {extension} не поддерживаются'
    except FileNotFoundError:
        logging.error(f'{datetime.datetime.now()}: Файл не найден')
        return 'Файл не найден.'
    except JSONDecodeError:
        logging.exception(f'{datetime.datetime.now()}')
        return 'Ошибка чтения файла JSON'
