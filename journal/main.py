def main():
    print_header()
    run_event_loop()


def print_header():
    print('----------------------------')
    print('     JOURNAL APP')
    print('----------------------------')


def run_event_loop():
    print('What do you want to do with your journal?')

    while 1:
        cmd = input('[L]ist entries, [A]dd an entry, E[x]it: ').lower().strip()
        if cmd == 'l':
            list_entries()
        elif cmd == 'a':
            add_entry()
        elif cmd == 'x':
            break
        else:
            print("Sorry, we don't understand '{}'".format(cmd))

    print('Done, goodbye.')


def list_entries():
    print("Listing......")


def add_entry():
    print("Adding.......")


main()
