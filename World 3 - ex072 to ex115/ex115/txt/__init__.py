from ex115.menu import head, line


def form(name, age, size=40):
    return f' {name[:int(f"{size - 7}")].ljust(int(f"{size - 6}"), " ")}|'\
           + f'{str(age):>3}\n'


def register(filename, name, age, size):
    try:
        file = open(filename, 'r')
    except FileNotFoundError:
        file = open(filename, 'w+')
        file.write(f'{line(size)}\n{form("NAME", "AGE", size)}{line(size)}\n')
        file.write(form(name, age, size))
    else:
        file = open(filename, 'a')
        file.write(form(name, age))
    finally:
        print('\033[32mNew record added successfully!\033[m')
        file.close()
    return file.name

def readfile(filename, size=40):
    try:
        file = open(filename, 'r+')
    except:
        print('\n\033[1:30:41m' + 'No Record!'.center(size) + '\033[m\n')
    else:
        print('\033[7m' + file.read(), end='')
        print(line(size) + '\n\033[m')
        input()
        file.close()