# Флаг Франции
RED = '\u001b[41m'
BLUE = '\u001b[44m'
WHITE = '\u001b[47m'
END = '\u001b[0m'
for i in range(6):
    print(BLUE + ' ' * 7 + WHITE + ' ' * 7 + RED + ' ' * 7 + END)

print('\n') # чтобы удобнее было смотреть на вывод в комадную строку

# Узор
PURPLE = '\u001b[45m'
BLACK = '\u001b[40m'
END = '\u001b[0m'


for i in range(2):
    print(BLACK + '     ' + PURPLE + '     ' + BLACK + '     ' + PURPLE + '     ' + BLACK + '     ' + END)
for i in range(2):
    print(PURPLE + '     ' + BLACK + '     ' + PURPLE + '     ' + BLACK + '     ' + PURPLE + '     ' + END)
for i in range(2):
    print(BLACK + '     ' + PURPLE + '     ' + BLACK + '     ' + PURPLE + '     ' + BLACK + '     ' + END)
print('\n')

# y=x^2
array = [['    ' for col in range(9)] for row in range(17)]
yes = []
xes = []
red ='\u001b[41m'
blue = '\u001b[44m'
nothing = '\u001b[0m'

for x in range(-4,5):
    y = x**2
    yes.append(y)
    xes.append(x)


for i in range(9):
    if len(str(i - 4)) == 2:
        array[-1][i] = blue + '  ' + str(i - 4) + nothing
    else:
        array[-1][i] = blue + '   ' + str(i - 4) + nothing

for i in range(17):
    if len(str(16 - i)) == 2:
        array[i][4] = blue + '  ' + str(16 - i) + nothing
    else:
        array[i][4] = blue + '   ' + str(16 - i) + nothing

for x1 in range(len(xes)):
    if len(str(yes[x1])) == 2:
        array[16 - yes[x1]][4 + xes[x1]] = red + '  ' + str(yes[x1]) + nothing
    else:
        array[16 - yes[x1]][4 + xes[x1]] = red + '   ' + str(yes[x1]) + nothing

for i in range(len(array)):
    for j in range(len(array[i])):
        print(array[i][j], end= ' ')
    print()
print('\n')

# Книги
red ='\u001b[41m'
blue = '\u001b[44m'
nothing = '\u001b[0m'

import csv

with open('books.csv') as csvfile:
    file_reader = csv.reader(csvfile, delimiter = ';')
    file = list(row for row in file_reader)[1:]
    before_2014 = 0
    after_2014 = 0
    all = 0
    for row in file:
        year = int(row[6][6:10])
        all += 1
        if year <= 2014:
            before_2014 += 1
        elif year > 2014:
            after_2014 += 1

percent_before_2014 = before_2014 / all * 100
percent_after_2014 = after_2014 / all * 100

array = [['    ' for col in range(10)] for row in range(11)]
for i in range(11):
    array[i][0] = str((10-i)*10) + '%'
    while len(array[i][0]) < 4:
        array[i][0] += ' '

for i in range(10):
    pr = (100 - i*10)
    if pr <= percent_after_2014:
        if pr <= percent_before_2014:
            print(blue + array[i][0] + nothing + '    ' + red + array[i][4] + nothing + '     ' + red + array[i][7] + nothing)
        else:
            print(blue + array[i][0] + nothing + '    ' + red + array[i][4] + nothing)
    else:
        print(blue + array[i][0] + nothing)
print(blue + '0%    до 2014  после 2014 ' + nothing)
