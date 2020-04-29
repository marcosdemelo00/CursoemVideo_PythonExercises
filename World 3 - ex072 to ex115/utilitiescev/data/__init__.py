def fnum(msg):
    while True:
        try:
            v = float(input(msg).strip().replace(',', '.'))
            return v
        except ValueError:
            print('Invalid value.')

#def fnum(msg):
#    valid = False
#    while not valid:
#        enter = str(input(msg)).replace(',', '.').strip()
#        if enter.isalpha() or enter == '':
#            print('Invalid value.')
#        else:
#            valid = True
#            return float(enter)
