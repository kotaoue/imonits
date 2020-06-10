# coding=utf8

import argparse
import glob
import os
import re

from modules.clitable import clitable


def get_args() -> (argparse.Namespace):
    parser = argparse.ArgumentParser(
        description='Search code and find "IMO" or "nits" level problem. by kotaoue')
    parser.add_argument(
        '-l', '--language', help='Target language.', type=str, default='PHP')
    parser.add_argument(
        '-d', '--directory', help='Target directory.', type=str, default='./')
    return parser.parse_args()


def print_list(language: str, directory: str):
    extensions_dict = {'PHP': '.php'}
    grep_dict = {
        'PHP': {
            'PHPDoc': ' \* (Class|Interface) ',
            'declaration': '(class|abstract class|interface|trait) '
        }
    }

    extension = extensions_dict.get(language, '')
    directory = '{0}/**/*{1}'.format(directory, extension)

    result = []

    files = glob.glob(directory, recursive=True)
    for file_path in files:
        file_name = os.path.basename(file_path)
        class_name = os.path.splitext(file_name)[0]

        row_item = {}
        row_item['file_path'] = file_path
        row_item['class_name'] = class_name

        with open(file_path) as file:
            for line in file.readlines():
                for grep_key, grep_value in grep_dict.get(language, {}).items():
                    row_item.setdefault(grep_key, 0)

                    re_pattern = '{0}{1}'.format(grep_value, class_name)
                    if re.match(re_pattern, line) is not None:
                        row_item[grep_key] += 1

        for grep_key in grep_dict.get(language, {}).keys():
            if row_item.get(grep_key, '0') != 1:
                result.append(row_item)
                break

    clitable.print_table(result)


def main():
    args = get_args()

    language = args.language
    directory = args.directory.rstrip('/')

    print_list(language=language, directory=directory)
    exit(0)


if __name__ == '__main__':
    main()
