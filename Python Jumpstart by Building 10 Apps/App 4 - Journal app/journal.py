import os

def load(name):
    data = []
    filename = get_path(name)
    if os.path.exists(filename):
        with open(filename) as file_data:
            for linha in file_data.readlines():
               data.append(linha.rstrip())

    return data

def save(name, journal_data):
    filename = get_path(name)
    print('...... retrieving path: {}'.format(filename))

    with open(filename, 'w') as fout:
        for entry in journal_data:
            fout.write(entry + '\n')


def get_path(name):
    filename = os.path.abspath(os.path.join('.', 'journals', name + '.jrl'))
    return filename


def add_entry(text, data):
    data.append(text)
