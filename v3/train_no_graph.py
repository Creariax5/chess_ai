import copy
import time
from ai import select_phase, move_phase, select_rnd, move_rnd


def play(w_network, b_network):
    time.sleep(0)

    class Piece:
        def __init__(self, team, type, nb, image, killable=False):
            self.team = team
            self.type = type
            self.nb = nb
            self.killable = killable
            self.image = image

    def create_board(board):
        board[0] = [Piece('b', 'r', 5, 'img/b_rook.png'), Piece('b', 'kn', 11, 'img/b_knight.png'),
                    Piece('b', 'b', 7, 'img/b_bishop.png'),
                    Piece('b', 'q', 3, 'img/b_queen.png'), Piece('b', 'k', 9, 'img/b_king.png'),
                    Piece('b', 'b', 7, 'img/b_bishop.png'),
                    Piece('b', 'kn', 11, 'img/b_knight.png'), Piece('b', 'r', 5, 'img/b_rook.png')]

        board[7] = [Piece('w', 'r', 6, 'img/w_rook.png'), Piece('w', 'kn', 12, 'img/w_knight.png'),
                    Piece('w', 'b', 8, 'img/w_bishop.png'),
                    Piece('w', 'q', 4, 'img/w_queen.png'), Piece('w', 'k', 10, 'img/w_king.png'),
                    Piece('w', 'b', 8, 'img/w_bishop.png'),
                    Piece('w', 'kn', 12, 'img/w_knight.png'), Piece('w', 'r', 6, 'img/w_rook.png')]

        for i in range(8):
            board[1][i] = Piece('b', 'p', 1, 'img/b_pawn.png')
            board[6][i] = Piece('w', 'p', 2, 'img/w_pawn.png')
        return board

    def on_board(position):
        if -1 < position[0] < 8 and -1 < position[1] < 8:
            return True

    def convert_to_readable(board):
        output = ''

        for i in board:
            for j in i:
                try:
                    output += j.team + j.type + ', '
                except:
                    output += j + ', '
            output += '\n'
        return output

    def convert_to_ai(board):
        my_input = []

        for i in range(14):
            my_input.append([])
            for j in range(8):
                my_input[i].append([])
                for k in range(8):
                    my_input[i][j].append(0)

        # w_pawn
        for i in range(8):
            for j in range(8):
                try:
                    if board[i][j].nb == 2:
                        my_input[0][i][j] = 1
                except:
                    my_input[0][i][j] = 0
        # w_pawn
        for i in range(8):
            for j in range(8):
                try:
                    if board[i][j].nb == 4:
                        my_input[1][i][j] = 1
                except:
                    my_input[1][i][j] = 0
        # w_pawn
        for i in range(8):
            for j in range(8):
                try:
                    if board[i][j].nb == 6:
                        my_input[2][i][j] = 1
                except:
                    my_input[2][i][j] = 0
        # w_pawn
        for i in range(8):
            for j in range(8):
                try:
                    if board[i][j].nb == 8:
                        my_input[3][i][j] = 1
                except:
                    my_input[3][i][j] = 0
        # w_pawn
        for i in range(8):
            for j in range(8):
                try:
                    if board[i][j].nb == 10:
                        my_input[4][i][j] = 1
                except:
                    my_input[4][i][j] = 0
        # w_pawn
        for i in range(8):
            for j in range(8):
                try:
                    if board[i][j].nb == 12:
                        my_input[5][i][j] = 1
                except:
                    my_input[5][i][j] = 0

        # b_pawn
        for i in range(8):
            for j in range(8):
                try:
                    if board[i][j].nb == 1:
                        my_input[6][i][j] = 1
                except:
                    my_input[6][i][j] = 0
        # b_pawn
        for i in range(8):
            for j in range(8):
                try:
                    if board[i][j].nb == 3:
                        my_input[7][i][j] = 1
                except:
                    my_input[7][i][j] = 0
        # b_pawn
        for i in range(8):
            for j in range(8):
                try:
                    if board[i][j].nb == 5:
                        my_input[8][i][j] = 1
                except:
                    my_input[8][i][j] = 0
        # b_pawn
        for i in range(8):
            for j in range(8):
                try:
                    if board[i][j].nb == 7:
                        my_input[9][i][j] = 1
                except:
                    my_input[9][i][j] = 0
        # b_pawn
        for i in range(8):
            for j in range(8):
                try:
                    if board[i][j].nb == 9:
                        my_input[10][i][j] = 1
                except:
                    my_input[10][i][j] = 0
        # b_pawn
        for i in range(8):
            for j in range(8):
                try:
                    if board[i][j].nb == 11:
                        my_input[11][i][j] = 1
                except:
                    my_input[11][i][j] = 0

        # w
        for i in range(8):
            for j in range(8):
                try:
                    if (board[i][j].nb % 2) == 0:
                        my_input[12][i][j] = 1
                except:
                    my_input[12][i][j] = 0
        # b
        for i in range(8):
            for j in range(8):
                try:
                    if (board[i][j].nb % 2) != 0:
                        my_input[13][i][j] = 1
                except:
                    my_input[13][i][j] = 0

        o = 0
        output = []
        for i in range(14):
            for j in range(8):
                for k in range(8):
                    output.append(my_input[i][j][k])

        return copy.deepcopy(output)

    def my_deselect(my_board):
        for row in range(len(my_board)):
            for column in range(len(my_board[0])):
                if my_board[row][column] == 'x ':
                    board[row][column] = '  '
                else:
                    try:
                        my_board[row][column].killable = False
                    except:
                        pass
        return convert_to_readable(my_board)

    def deselect():
        for row in range(len(board)):
            for column in range(len(board[0])):
                if board[row][column] == 'x ':
                    board[row][column] = '  '
                else:
                    try:
                        board[row][column].killable = False
                    except:
                        pass
        return convert_to_readable(board)

    def highlight(board):
        highlighted = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'x ':
                    highlighted.append((i, j))
                else:
                    try:
                        if board[i][j].killable:
                            highlighted.append((i, j))
                    except:
                        pass
        return highlighted

    def check_team(moves, index):
        row, col = index
        if moves % 2 == 0:
            if board[row][col].team == 'w':
                return True
        else:
            if board[row][col].team == 'b':
                return True

    def select_moves(piece, index, moves):
        if check_team(moves, index):
            if piece.type == 'p':
                if piece.team == 'b':
                    return highlight(pawn_moves_b(index))
                else:
                    return highlight(pawn_moves_w(index))

            if piece.type == 'k':
                return highlight(king_moves(index))

            if piece.type == 'r':
                return highlight(rook_moves(index))

            if piece.type == 'b':
                return highlight(bishop_moves(index))

            if piece.type == 'q':
                return highlight(queen_moves(index))

            if piece.type == 'kn':
                return highlight(knight_moves(index))

    def pawn_moves_b(index):
        if index[0] == 1:
            if board[index[0] + 2][index[1]] == '  ' and board[index[0] + 1][index[1]] == '  ':
                board[index[0] + 2][index[1]] = 'x '
        bottom3 = [[index[0] + 1, index[1] + i] for i in range(-1, 2)]

        for positions in bottom3:
            if on_board(positions):
                if bottom3.index(positions) % 2 == 0:
                    try:
                        if board[positions[0]][positions[1]].team != 'b':
                            board[positions[0]][positions[1]].killable = True
                    except:
                        pass
                else:
                    if board[positions[0]][positions[1]] == '  ':
                        board[positions[0]][positions[1]] = 'x '
        return board

    def pawn_moves_w(index):
        if index[0] == 6:
            if board[index[0] - 2][index[1]] == '  ' and board[index[0] - 1][index[1]] == '  ':
                board[index[0] - 2][index[1]] = 'x '
        top3 = [[index[0] - 1, index[1] + i] for i in range(-1, 2)]

        for positions in top3:
            if on_board(positions):
                if top3.index(positions) % 2 == 0:
                    try:
                        if board[positions[0]][positions[1]].team != 'w':
                            board[positions[0]][positions[1]].killable = True
                    except:
                        pass
                else:
                    if board[positions[0]][positions[1]] == '  ':
                        board[positions[0]][positions[1]] = 'x '
        return board

    def king_moves(index):
        for y in range(3):
            for x in range(3):
                if on_board((index[0] - 1 + y, index[1] - 1 + x)):
                    if board[index[0] - 1 + y][index[1] - 1 + x] == '  ':
                        board[index[0] - 1 + y][index[1] - 1 + x] = 'x '
                    else:
                        if board[index[0] - 1 + y][index[1] - 1 + x].team != board[index[0]][index[1]].team:
                            board[index[0] - 1 + y][index[1] - 1 + x].killable = True
        return board

    def rook_moves(index):
        cross = [[[index[0] + i, index[1]] for i in range(1, 8 - index[0])],
                 [[index[0] - i, index[1]] for i in range(1, index[0] + 1)],
                 [[index[0], index[1] + i] for i in range(1, 8 - index[1])],
                 [[index[0], index[1] - i] for i in range(1, index[1] + 1)]]

        for direction in cross:
            for positions in direction:
                if on_board(positions):
                    if board[positions[0]][positions[1]] == '  ':
                        board[positions[0]][positions[1]] = 'x '
                    else:
                        if board[positions[0]][positions[1]].team != board[index[0]][index[1]].team:
                            board[positions[0]][positions[1]].killable = True
                        break
        return board

    def bishop_moves(index):
        diagonals = [[[index[0] + i, index[1] + i] for i in range(1, 8)],
                     [[index[0] + i, index[1] - i] for i in range(1, 8)],
                     [[index[0] - i, index[1] + i] for i in range(1, 8)],
                     [[index[0] - i, index[1] - i] for i in range(1, 8)]]

        for direction in diagonals:
            for positions in direction:
                if on_board(positions):
                    if board[positions[0]][positions[1]] == '  ':
                        board[positions[0]][positions[1]] = 'x '
                    else:
                        if board[positions[0]][positions[1]].team != board[index[0]][index[1]].team:
                            board[positions[0]][positions[1]].killable = True
                        break
        return board

    def queen_moves(index):
        board = rook_moves(index)
        board = bishop_moves(index)
        return board

    def knight_moves(index):
        for i in range(-2, 3):
            for j in range(-2, 3):
                if i ** 2 + j ** 2 == 5:
                    if on_board((index[0] + i, index[1] + j)):
                        if board[index[0] + i][index[1] + j] == '  ':
                            board[index[0] + i][index[1] + j] = 'x '
                        else:
                            if board[index[0] + i][index[1] + j].team != board[index[0]][index[1]].team:
                                board[index[0] + i][index[1] + j].killable = True
        return board

    class Node:
        def __init__(self, row, col, width):
            self.row = row
            self.col = col
            self.x = int(row * width)
            self.y = int(col * width)
            self.colour = WHITE
            self.occupied = None

        def setup(self, WIN):
            if starting_order[(self.row, self.col)]:
                if starting_order[(self.row, self.col)] is None:
                    pass
                else:
                    WIN.blit(starting_order[(self.row, self.col)], (self.x, self.y))

    def make_grid(rows, width):
        grid = []
        gap = WIDTH // rows
        for i in range(rows):
            grid.append([])
            for j in range(rows):
                node = Node(j, i, gap)
                grid[i].append(node)
                if (i + j) % 2 == 1:
                    grid[i][j].colour = GREY
        return grid

    def Do_Move(OriginalPos, FinalPosition):
        starting_order[FinalPosition] = starting_order[OriginalPos]
        starting_order[OriginalPos] = None

    def remove_highlight(grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i + j) % 2 == 0:
                    grid[i][j].colour = WHITE
                else:
                    grid[i][j].colour = GREY
        return grid

    def test_possibility(moves, my_board):
        def up(y, x):
            if y < 7:
                y += 1
            else:
                y = 0
                x += 1
            return y, x

        possibility_table = []

        y1 = 0
        x1 = 0

        while x1 * y1 != 50:
            try:
                possible = select_moves((my_board[x1][y1]), (x1, y1), moves)
                for positions in possible:
                    row, col = positions
                    new_board = copy.deepcopy(my_board)
                    new_board[row][col] = new_board[x1][y1]
                    new_board[x1][y1] = '  '
                    deselect()
                    tab = [[convert_to_ai(new_board)], [x1, y1, row, col]]
                    possibility_table.append(tab)
                y1, x1 = up(y1, x1)
            except:
                y1, x1 = up(y1, x1)
        return possibility_table

    def main(WIDTH, w_network, b_network):
        moves = 0
        selected = False
        piece_to_move = []
        grid = make_grid(8, WIDTH)
        win = 0
        while win == 0:
            if not selected:
                if moves % 2 == 0:
                    # all the possibility for 1 move in possibility
                    possibility = test_possibility(2, board)
                    score_list = []

                    # [score returned by forward_propagation, coordinate to this move] append to score_list
                    for i in range(len(possibility)):
                        score_tab = [select_phase(possibility[i][0][0], w_network), possibility[i][1]]
                        score_list.append(score_tab)

                    # in best_score the best score and in score_index the index to get his score_list
                    best_score = 0
                    score_index = 0
                    for i in range(len(score_list)):
                        sl = score_list[i][0][0]
                        if sl > best_score:
                            best_score = sl
                            score_index = i
                    x, y, x_next, y_next = score_list[score_index][1]
                else:
                    y, x = select_rnd()
                try:
                    possible = select_moves((board[x][y]), (x, y), moves)
                    for positions in possible:
                        row, col = positions
                        grid[row][col].colour = BLUE
                    piece_to_move = x, y
                    selected = True
                except:
                    piece_to_move = []
            else:
                if moves % 2 == 0:
                    y, x = y_next, x_next
                else:
                    y, x = move_rnd()
                try:
                    if board[x][y].killable:
                        row, col = piece_to_move
                        if moves % 2 == 0:
                            try:
                                if board[x][y].nb == 9:
                                    win = 1
                                    print("WHITE win in ", moves, " moves")
                            except:
                                pass
                        if moves % 2 != 0:
                            try:
                                if board[x][y].nb == 10:
                                    win = 2
                                    print("BLACK win in ", moves, " moves")
                            except:
                                pass
                        board[x][y] = board[row][col]
                        board[row][col] = '  '
                        deselect()
                        remove_highlight(grid)
                        Do_Move((col, row), (y, x))
                        moves += 1
                    else:
                        deselect()
                        remove_highlight(grid)
                except:
                    if board[x][y] == 'x ':
                        row, col = piece_to_move
                        if moves % 2 == 0:
                            try:
                                if board[x][y].nb == 9:
                                    win = 1
                                    print("WHITE win in ", moves, " moves")
                            except:
                                pass
                        if moves % 2 != 0:
                            try:
                                if board[x][y].nb == 10:
                                    win = 2
                                    print("BLACK win in ", moves, " moves")
                            except:
                                pass
                        board[x][y] = board[row][col]
                        board[row][col] = '  '
                        deselect()
                        remove_highlight(grid)
                        Do_Move((col, row), (y, x))
                        moves += 1
                    else:
                        deselect()
                        remove_highlight(grid)
                selected = False
                if moves > 80:
                    win = 3
                    print("EQUALITY ", moves, " moves")
        return w_network, b_network, win

    board = [['  ' for i in range(8)] for j in range(8)]

    starting_order = {(0, 0): "br", (1, 0): "bkn",
                      (2, 0): "bb", (3, 0): "bk",
                      (4, 0): "bq", (5, 0): "bb",
                      (6, 0): "bkn", (7, 0): "br",
                      (0, 1): "bp", (1, 1): "bp",
                      (2, 1): "bp", (3, 1): "bp",
                      (4, 1): "bp", (5, 1): "bp",
                      (6, 1): "bp", (7, 1): "bp",

                      (0, 2): None, (1, 2): None, (2, 2): None, (3, 2): None,
                      (4, 2): None, (5, 2): None, (6, 2): None, (7, 2): None,
                      (0, 3): None, (1, 3): None, (2, 3): None, (3, 3): None,
                      (4, 3): None, (5, 3): None, (6, 3): None, (7, 3): None,
                      (0, 4): None, (1, 4): None, (2, 4): None, (3, 4): None,
                      (4, 4): None, (5, 4): None, (6, 4): None, (7, 4): None,
                      (0, 5): None, (1, 5): None, (2, 5): None, (3, 5): None,
                      (4, 5): None, (5, 5): None, (6, 5): None, (7, 5): None,

                      (0, 6): "wp", (1, 6): "wp",
                      (2, 6): "wp", (3, 6): "wp",
                      (4, 6): "wp", (5, 6): "wp",
                      (6, 6): "wp", (7, 6): "wp",
                      (0, 7): "wr", (1, 7): "wkn",
                      (2, 7): "wb", (3, 7): "wk",
                      (4, 7): "wk", (5, 7): "wb",
                      (6, 7): "wkn", (7, 7): "wr", }

    WIDTH = 800

    WHITE = (180, 165, 255)
    GREY = (45, 0, 180)
    BLUE = (150, 200, 200)

    create_board(board)

    return main(WIDTH, w_network, b_network)
