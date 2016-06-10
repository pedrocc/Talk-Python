import journal


def main():
    print_header()
    run_event_loop()

def print_header():
    print('------------------------------------------')
    print('         PERSONAL JOURNAL APP')
    print('------------------------------------------')



def run_event_loop():
    print('What do you want to do with your journal?')
    journal_name = 'default'
    journal_data = journal.load(journal_name)

    while True:
        cmd = input('[L]ist entries, [A}dd an entry, E[x]it: ')
        cmd = cmd.lower().strip()
        if cmd == 'l':l
            list_entries(journal_data)
        elif cmd == 'a':
            add_entry(journal_data)

        elif cmd == 'x':
            print('Done, goodbye.')

            break
        else:
            print('Erro na aplicação, não existe o comento: ', cmd)
        journal.save(journal_name, journal_data)

def list_entries(data):
    data = reversed(data)
    for index, lines in enumerate(data):
        print('* [{}] {}'.format(index + 1, lines))

def add_entry(data):
    text = input('Type your entry, <enter> to exit: ')
    journal.add_entry(text, data)






main()