import json
import logging


def save_post_to_json(picture, text):
    '''
    Сохранение нового поста в JSON
    args: picture - объект картинка, полученный через post запрос
          text - текст поста
    returns: True или False в зависимости от результата записи
    '''


    try:
        filename = picture.filename
        picture.save(f'./uploads/images/{filename}')
        new_data = {'pic': f'./uploads/images/{filename}',
                    'content': text}

        with open('posts.json', encoding='utf-8') as file:
            data = json.load(file)
            data.append(new_data)

        with open('posts.json', 'w', encoding='utf-8') as file1:
            json.dump(data, file1, indent=4,
                      separators=(',', ': '),
                      ensure_ascii=False)
    except:
        return False
    else:
        return True


def set_upload_logger():
    '''
        Создание логера загрузки файлов с неподдерживаемым форматом
        args:
        returns: объект логгер
        '''

    logger = logging.getLogger('upload_logger')
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s : %(message)s")
    file_handler = logging.FileHandler('./upload_log.txt', encoding='utf-8')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.info('Начало записи')

    return logger

