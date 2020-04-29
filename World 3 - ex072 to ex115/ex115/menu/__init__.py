from time import sleep

def line(size):
    return '-' * size


def head(txt, size):
    headmsg = line(size)
    headmsg += '\n\033[1:34m' + txt.center(size).upper() + '\033[m\n'
    headmsg += line(size)
    return headmsg


def menu(list, size):
    print(head('register sistem', size))
    for c, i in enumerate(list):
        print(f'\033[33m[ {c + 1} ]\033[m - \033[34m{i}\033[m')
    print(line(size))
    sleep(0.5)
    opt = readint('\033[32mEnter a option: \033[m', len(list))
    return opt


def readint(msg, options=0):
    while True:
        try:
            v = int(input(msg).strip())
        except (ValueError, TypeError):
            print('\033[1:31mInvalid Option!\033[m')
        except KeyboardInterrupt:
            print('\033[31mProgram interrupted by user.\033[m')
            break
        else:
            if options == 0:
                return v
            elif v in range(1, options + 1):
                return v
            else:
                print('\033[1:31mInvalid Option!\033[m')


def areyousure(name, age, size):
    while True:
        valid = input(f'Confirm {name} - {age}? [Y/N]').strip().lower()
        if valid in ('yes', 'y', ''):
            return True
        elif valid in ('no', 'n'):
            print(line(size))
            return False

