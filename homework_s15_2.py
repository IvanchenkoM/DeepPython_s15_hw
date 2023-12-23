# Напишите код, который запускается из командной строки и получает на вход путь до
# директории на ПК. Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# * имя файла без расширения или название каталога,
# * расширение, если это файл,
# * флаг каталога,
# * название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя логирование.
import os
import logging
from collections import namedtuple

FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_dir', 'parent_directory'])


def get_file_info(path):
    logging.basicConfig(filename='hw2_log.log', level=logging.INFO, encoding='utf-8',
                        format='%(asctime)s - %(message)s')
    logger = logging.getLogger('hw2_log')

    try:
        items = os.listdir(path)
        file_info_list = []

        for item in items:
            item_path = os.path.join(path, item)
            is_dir = os.path.isdir(item_path)
            parent_dir = os.path.basename(os.path.normpath(path))

            if is_dir:
                name = item
                extension = "Папка"
            else:
                name, extension = os.path.splitext(item)

            file_info = FileInfo(name, extension, is_dir, parent_dir)
            file_info_list.append(file_info)

            logger.info(file_info)

        return file_info_list
    except Exception as e:
        logger.error(f"Ошибка: {e}")
        return []


def main():
    import sys
    if len(sys.argv) < 2:
        print("Используйте: python homework_s15_2.py Путь до папки")
        return

    directory_path = sys.argv[1]

    if not os.path.exists(directory_path):
        print("Папка не существует.")
        return

    get_file_info(directory_path)

    print("Информация в файле hw2_log.log.")


if __name__ == "__main__":
    main()