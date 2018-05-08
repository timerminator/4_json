import json
import pprint


def load_json(filepath):
    with open(filepath, encoding='utf-8') as json_content:
        return json.load(json_content)


def pretty_print_json(json_data):
    pprint.pprint(json_data)


if __name__ == '__main__':
    pretty_print_json(load_json(input("Input path: ")))
