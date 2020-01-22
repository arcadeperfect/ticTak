class Game(object):

    def __init__(self):

        self.state = "init"
        self.playerState = None
        self.board = Board()
        self.winner = None

    def game_loop(self):

        if self.playerState == None:
            # first loop
            self.playerState = 1

        if self.board.winner is not False:
            print("winner is ", self.board.winner)
            self.winner = self.board.winner
            return

        if self.playerState == 1 and self.winner == None:
            print("player 1")

            # get player 1 input

            turn_taken = False
            while turn_taken == False:
                string = input()
                x, y = int(string[0]), int(string[1])
                if self.board.set_player_1(x, y):
                    self.board.print_matrix()
                    turn_taken = True
                    self.playerState = 2
                else:
                    print("space not empty")
            self.winner = self.board.check_for_win()

        if self.playerState == 2  and self.winner == None:
            print("player 2")

            # get player 2 input
            turn_taken = False
            while turn_taken == False:
                string = input()
                x, y = int(string[0]), int(string[1])
                if self.board.set_player_2(x, y):
                    self.board.print_matrix()
                    turn_taken = True
                    self.playerState = 1
                else:
                    print("space not empty")
            self.winner = self.board.check_for_win()


class Board(object):

    def __init__(self):

        self.w = 3
        self.h = 3

        self.matrix = [[0 for x in range(self.w)] for y in range(self.h)]

        self.winner = False

    # todo: breaks when you try to play out of bounds

    def set_player_1(self, x, y):
        cell = self.check_cell(x, y)
        if not cell:
            if self.within_board(x, y):
                self.matrix[x][y] = 1
                #self.check_for_win()
                return True
            else:
                print("out of bounds")
                return False
        else:
            return False

    def set_player_2(self, x, y):
        cell = self.check_cell(x, y)
        if not cell:
            if self.within_board(x, y):
                self.matrix[x][y] = 2
                #self.check_for_win()
                return True
            else:
                print("out of bounds")
                return False
        else:
            return False

    def check_cell(self, x, y):
        if not self.matrix[x][y] == 0:

            return self.matrix[x][y]
        else:
            return False

    def within_board(self, x, y):  # make sure new coords aren't out of range of the array
        if x < self.w and y < self.h and min([x, y]) >= 0:
            return True
        else:
            return False

    def get_neighbors(self, x, y):  # find all neigbouring cell coords

        neighbours = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                dx = x + i
                dy = y + j
                if [dx, dy] != [x, y]:
                    if self.within_board(dx, dy):
                        neighbours.append((dx, dy))
        return neighbours

    def check_for_win(self, x=None, y=None, vx=None, vy=None, player=None, depth = 0):
        # recursively check for the winner
        # todo: currently only works for 3 x 3 because it only checks if you have hit the edge
        #  doesn't count number of wins

        # if no vector supplied, therefore first recursive level

        if vx is None or vy is None and won is False:

            # initial loop only start along the edges, bc false positive if we start from the center
            depth = 1
            to_check = [[x, 0] for x in range(self.w)]
            to_check += [[0, y] for y in range(self.h)]

            for x, y in to_check:

                # check for a play in this spot

                cell_1 = self.check_cell(x, y)
                if cell_1:

                    # if cell isn't empty, get all the neighbors. Returns list of (x,y) tuples

                    for i in self.get_neighbors(x, y):
                        x2 = i[0]
                        y2 = i[1]
                        cell_2 = self.check_cell(x2, y2)
                        if cell_2 == cell_1:
                            vx = x2 - x
                            vy = y2 - y
                            print("checking", x2,y2)
                            return self.check_for_win(x2, y2, vx, vy, cell_1, 1)

        # if params are specified, keep checking in that direction based on the vector

        else:
            depth += 1
            # print("depth", depth)

            cell_1 = self.check_cell(x, y)
            if cell_1 == player:
                x2 = x + vx
                y2 = y + vy

                if depth == self.w:
                    print("winner is", player)
                    self.winner = player
                    return player

                else:
                    print("checking", x2, y2)
                    return self.check_for_win(x2, y2, vx, vy, player, depth)



        # else:
        #     depth += 1
        #     print("depth", depth)
        #
        #     cell_1 = self.check_cell(x, y)
        #     if cell_1 == player:
        #         x2 = x + vx
        #         y2 = y + vy
        #         if self.within_board(x2, y2):
        #             print(x2,y2, "is within board")
        #             return self.check_for_win(x2, y2, vx, vy, player, depth)
        #         else:
        #             if depth == self.w:
        #                 print("winner is", player)
        #                 self.winner = player
        #                 return player

    def print_matrix(self):
        for y in reversed(range(self.h)):
            for x in range(self.w):
                print(self.matrix[x][y], end="")
            print("")

    def update(self):
        self.print_matrix()
        self.check_for_win()


if __name__ == "__main__":
    game = Game()

    while game.winner is None:
        game.game_loop()