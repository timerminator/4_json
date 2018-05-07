import json
import pprint


def load_data(filepath):
    with open(filepath, encoding='utf-8') as file:
        return json.load(file)


def pretty_print_json(data):
    pprint.pprint(data)


if __name__ == '__main__':
    pretty_print_json(load_data(input("Input path: ")))
