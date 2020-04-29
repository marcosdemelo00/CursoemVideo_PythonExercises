print('\033[1:33mSimple\033[m and \033[7:31museful\033[m '
      '\033[31mc\033[32mo\033[33ml\033[34mo\033[35mr\033[36ms\033[m '
      'to use on \033[1:30:44mPython Terminal\033[m')
style = {'none': 0, 'bold': 1, 'underline': 4, 'negative':7}
text = {
    'white': '30',
    'red': '31',
    'green': '32',
    'yellow': '33',
    'blue': '34',
    'purple': '35',
    'cyan': '36',
    'gray': '37'
}
back = {
    'white': '40',
    'red': '41',
    'green': '42',
    'yellow': '43',
    'blue': '44',
    'purple': '45',
    'cyan': '46',
    'gray': '47'
}
clean = '\033[m'
print('Very {}cool{} isn\'t it?'.format('\033[' + text['yellow'] + 'm', clean))