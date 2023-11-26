import json
from wiki_data_source import get_content


def _write_to_file(data, filename='medical.json'):
    filename='./data_source/data/'+filename
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def read_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def prepare_data():
    _write_to_file(get_content(number=1,medical=True))
    _write_to_file(data=get_content(number=1,medical=False),filename='non_medical.json')

prepare_data()