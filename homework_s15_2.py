# Напишите код, который запускается из командной строки и получает на вход путь до
# директории на ПК. Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# * имя файла без расширения или название каталога,
# * расширение, если это файл,
# * флаг каталога,
# * название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя логирование.
import os
import argparse
import logging
from collections import namedtuple

logging.basicConfig(filename='hw2_log.log', level=logging.INFO, encoding='utf-8', format='%(asctime)s - %(message)s')
logger = logging.getLogger('hw2_log')

FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent_directory'])


def parse_directory(directory_path):
    try:
        if not os.listdir(directory_path):
            raise Exception("Пустая директория")
        if not os.path.isdir(directory_path):
            raise FileNotFoundError("Директория не найдена")

        entries = []

        for entry in os.scandir(directory_path):
            if entry.is_file():
                name, extension = os.path.splitext(entry.name)
                is_directory = False
            else:
                name = entry.name
                extension = "folder"
                is_directory = True
            parent_directory = os.path.basename(directory_path)
            obj = FileInfo(name, extension, is_directory, parent_directory)
            entries.append(obj)
            logger.info(obj)
        return entries
    except FileNotFoundError:
        logging.exception(f"Директория не найдена: {directory_path}")
    except Exception as e:
        logging.exception(f"An error occurred: {str(e)}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('directory', help='Path to the directory')
    args = parser.parse_args()

    directory_path = args.directory

    entries = parse_directory(directory_path)