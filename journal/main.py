import journal


def main():
    print_header()
    run_event_loop()


def print_header():
    print('----------------------------')
    print('     JOURNAL APP')
    print('----------------------------')


def run_event_loop():
    print('What do you want to do with your journal?')

    journal_name = 'default'
    journal_data = journal.load(journal_name)

    while True:
        cmd = input('[L]ist entries, [A]dd an entry, E[x]it: ').lower().strip()
        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entry(journal_data)
        elif cmd == 'x' or not cmd:
            break
        else:
            print("Sorry, we don't understand '{}'".format(cmd))

    print('Done, goodbye.')
    journal.save(journal_name, journal_data)


def list_entries(data):
    print('Your journal entries')
    entries = reversed(data)
    for idx, entry in enumerate(entries):
        print('* [{}] {}'.format(idx+1, entry))


def add_entry(data):
    text = input("Type your entry, <enter> to exit: ")
    journal.add_entry(text, data)


if __name__ == '__main__':
    # if you are executing this program and not importing it
    main()
