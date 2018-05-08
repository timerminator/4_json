import json
import sys

def load_json(filepath):
    with open(filepath, encoding='utf-8') as file:
        return json.load(file)


def pretty_print_json(data):
    print(json.dumps(data, sort_keys=True, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    try:
        pretty_print_json(load_json(sys.argv[1]))
    except IndexError as e:
        print('Вы не указали путь к файлу')
    except IOError as e:
        print('Не удалось открыть файл')
    except json.decoder.JSONDecodeError:
        print('Указанный файл не в формате json')