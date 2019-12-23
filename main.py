import keyboard

w = 3
h = 3
player = 1

board = [[None for x in range(w)] for y in range(h)]


# active = [0,0]


def dt(x, y):
    this = board[x][y]
    # if active[0] == x and active[1] == y:
    #     #return (u"\u2588")
    #     pass
    # if this == None:
    #     return (" ")
    # elif this == 2:
    #     return ("o")
    # elif this == 1:
    #     return ("x")
    # else:
    #     return("?")
    return this


def update_display():
    print(dt(0, 2), "|", dt(1, 2), "|", dt(2, 2))
    print("_________")
    print(dt(0, 1), "|", dt(1, 1), "|", dt(2, 1))
    print("_________")
    print(dt(0, 0), "|", dt(1, 0), "|", dt(2, 0))
    print("player {} enter coords".format(player))


# def detect_win():


c = 0
for y in range(w):
    for x in range(h):
        board[x][y] = c
        c += 1
#
# board[1][0] = 1
# board[1][1] = 1
# board[1][2] = 1

board[2][0] = 1
board[2][1] = 1
board[2][2] = 1

def within_board(x, y):  # make sure new coords aren't out of range of the array
    if x < w and y < h and min([x, y]) >= 0:
        return True
    else:
        return False


def getNeighbours(x, y):  # find all neigbouring cell coords

    neighbours = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            dx = x + i
            dy = y + j
            if [dx, dy] != [x, y]:
                if within_board(dx, dy):
                    neighbours.append([dx, dy])
    return neighbours


# for x in range(w):
#     for y in range(h):
won = False

x=1
y=0

def testWin():

    for x in range(w):
        for y in range(h):

            this_cell = board[x][y]

            for i in getNeighbours(x, y):
                dx, dy = i[0], i[1]
                newCell = board[dx][dy]
                vector = [dx-x,dy-y]

                if newCell == this_cell:
                    print("match")
                    newNewCellCoodrs = [dx+vector[0],dy+vector[1]]

                    if newNewCellCoodrs[0] < w and newNewCellCoodrs[1] < h:
                        if board[dx+vector[0]][dy+vector[1]] == this_cell:
                            print("win")
                            won = True
                            return True

testWin()

update_display()

# player = 1
# while True:
#
#     inp = input()
#     x = int(inp[0])-1
#     y = int(inp[1])-1
#     # active[0] = x
#     # active[1] = y
#     board[x][y] = player
#
#     update_display()
#
#
#
#     if player == 1:
#         player = 2
#
#     elif player == 2:
#         player =1
