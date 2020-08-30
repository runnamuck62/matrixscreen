import curses
import time
from random import randint, choice

# Character list for trail
chars = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']

# Length of character trail


class Trails():
    def __init__(self, tr_length, xval):
        self.length = tr_length
        self.xval = xval
        self.yval = 0

def node_spawner():
    chance = randint(1,10)
    if chance <= 5:
        return True
    else:
        return False


def matrix(root):
    curses.curs_set(0)
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    root.bkgd(curses.color_pair(1))
    root.immedok(True)
    active_cols = []
    to_remove = []
    height, width = root.getmaxyx()
    while True:
        if len(active_cols) > width:
            active_cols.pop(0)
        if node_spawner():
            tr_length = randint(7, height // 2)
            column = randint(2, width - 3)
            if chr(root.inch(0,column) != ' '):
                active_cols.append(Trails(tr_length, column))
        for i in range(len(active_cols)):
            y = active_cols[i].yval
            x = active_cols[i].xval
            length = active_cols[i].length
            if y < height and y <= length:
                root.addch(y, x, choice(chars))
                active_cols[i].yval += 1

            elif height > y >= length:
                root.addch(y, x, choice(chars))
                active_cols[i].yval += 1
                root.addch(y - length -1, x, ' ')

            elif height <= y <= height + length:
                active_cols[i].yval += 1
                root.addch(y - length - 1, x, ' ')

            elif y > height + length + 1:
                root.addch(y - length - 2 , x, ' ')




        time.sleep(.05)




def main(root):
    matrix(root)


curses.wrapper(main)
