w = 6
h = 6

matrix = [[0 for x in range(w)] for y in range(h)]


def check_cell(x, y):
    if not matrix[x][y] == 0:

        return matrix[x][y]
    else:
        return False


# def check_matrix(x,y):
#
#     width = w
#     height = h
#
#     print(check_space(x, y))


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
                    neighbours.append((dx, dy))
    return neighbours


def check_for_win(x=None, y=None, vx=None, vy=None, player=None):

    # recursively check for the winner
    # todo: currently only works for 3 x 3 because it only checks if you have hit the edge, doesn't count number of wins


    # if no vector supplied, therefore first recursive level
    won = False
    if vx == None or vy == None and won == False:

        # initial loop only start along the edges, bc false positive if we start from the center

        to_check = [[x, 0] for x in range(w)]
        to_check += [[0, y] for y in range(h)]

        for x, y in to_check:

            # check for a play in this spot

            cell_1 = check_cell(x, y)
            if cell_1:

                # if cell isn't empty, get all the neighbors. Returns list of (x,y) tuples

                for i in getNeighbours(x, y):
                    x2 = i[0]
                    y2 = i[1]
                    cell_2 = check_cell(x2, y2)
                    if cell_2 == cell_1:
                        vx = x2 - x
                        vy = y2 - y
                        return check_for_win(x2, y2, vx, vy, cell_1)

    # if params are specified, keep checking in that direction based on the vector

    else:
        cell_1 = check_cell(x, y)
        if cell_1 == player:
            x2 = x + vx
            y2 = y + vy
            if within_board(x2, y2):
                return check_for_win(x2, y2, vx, vy, player)
            else:
                #print("winner is", player)
                return player


def print_matrix():
    for y in reversed(range(h)):
        for x in range(w):
            print(matrix[x][y], end="")
        print("")


matrix[0][0] = 1
matrix[1][0] = 1
matrix[2][0] = 1
matrix[3][0] = 1
matrix[4][0] = 1
matrix[5][0] = 1

print_matrix()

print(check_for_win())
