import json
import pprint


def load_data(filepath):
    with open(filepath, encoding='utf-8') as json_content:
        return json.load(json_content)


def pretty_print_json(data):
    pprint.pprint(data)


if __name__ == '__main__':
    pretty_print_json(load_data(input("Input path: ")))
