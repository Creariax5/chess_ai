import sys
import pygame
from ai import select_phase, move_phase, select_rnd, move_rnd


def play(network):
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
        output = []

        for i in board:
            for j in i:
                try:
                    output.append(j.nb)
                except:
                    output.append(0)
        return output

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

        def draw(self, WIN):
            pygame.draw.rect(WIN, self.colour, (self.x, self.y, WIDTH / 8, WIDTH / 8))

        def setup(self, WIN):
            if starting_order[(self.row, self.col)]:
                if starting_order[(self.row, self.col)] is None:
                    pass
                else:
                    WIN.blit(starting_order[(self.row, self.col)], (self.x, self.y))

    def make_grid(rows, width):
        grid = []
        gap = WIDTH // rows
        print(gap)
        for i in range(rows):
            grid.append([])
            for j in range(rows):
                node = Node(j, i, gap)
                grid[i].append(node)
                if (i + j) % 2 == 1:
                    grid[i][j].colour = GREY
        return grid

    def draw_grid(win, rows, width):
        gap = width // 8
        for i in range(rows):
            pygame.draw.line(win, BLACK, (0, i * gap), (width, i * gap))
            for j in range(rows):
                pygame.draw.line(win, BLACK, (j * gap, 0), (j * gap, width))

    def update_display(win, grid, rows, width):
        for row in grid:
            for spot in row:
                spot.draw(win)
                spot.setup(win)
        draw_grid(win, rows, width)
        pygame.display.update()

    def Find_Node(pos, WIDTH):
        interval = WIDTH / 8
        y, x = pos
        rows = y // interval
        columns = x // interval
        return int(rows), int(columns)

    def display_potential_moves(positions, grid):
        for i in positions:
            x, y = i
            grid[x][y].colour = BLUE
            """
            Displays all the potential moves
            """

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

    def kill():
        print("You kill a pawn")

    def killed():
        print("one of your pawn as been killed")

    def win():
        print("You win")

    def lose():
        print("You lose")

    def main(WIN, WIDTH, w_network):
        ai = True
        moves = 0
        selected = False
        piece_to_move = []
        grid = make_grid(8, WIDTH)

        i = 1
        while i != 5:
            pygame.time.delay(0)
            i += 1
            print(i)
            # if event.type == pygame.MOUSEBUTTONDOWN:
            if ai:
                if not selected:
                    if moves % 2 == 0:
                        y, x = select_phase(convert_to_ai(board), w_network[0], 0)
                    else:
                        y, x = select_rnd()
                    try:
                        possible = select_moves((board[x][y]), (x, y), moves)
                        for positions in possible:
                            row, col = positions
                            grid[row][col].colour = BLUE
                        piece_to_move = x, y
                        selected = True
                        if moves % 2 == 0:
                            w_network[1] += 3
                        # else:
                        # b_network[1] += 3
                    except:
                        piece_to_move = []
                        print('Can\'t select')
                        if moves % 2 == 0:
                            w_network[1] += -1
                        # else:
                        # b_network[1] += -1
                    # print(piece_to_move)

                else:
                    if moves % 2 == 0:
                        y, x = move_phase(convert_to_ai(board), w_network[0], 0)
                    else:
                        y, x = move_rnd()
                    try:
                        if board[x][y].killable:
                            row, col = piece_to_move  # coords of original piece
                            board[x][y] = board[row][col]
                            board[row][col] = '  '
                            deselect()
                            remove_highlight(grid)
                            Do_Move((col, row), (y, x))
                            moves += 1
                            if moves % 2 == 0:
                                w_network[1] += 12
                            # else:
                            # b_network[1] += 12
                        else:
                            deselect()
                            remove_highlight(grid)
                            selected = False
                            print("Deselected")
                            if moves % 2 == 0:
                                w_network[1] += -2
                            # else:
                            # b_network[1] += -2
                    except:
                        if board[x][y] == 'x ':
                            row, col = piece_to_move
                            board[x][y] = board[row][col]
                            board[row][col] = '  '
                            deselect()
                            remove_highlight(grid)
                            Do_Move((col, row), (y, x))
                            moves += 1
                            if moves % 2 == 0:
                                w_network[1] += 12
                            # else:
                            # b_network[1] += 12
                        else:
                            deselect()
                            remove_highlight(grid)
                            selected = False
                            print("Invalid move")
                            if moves % 2 == 0:
                                w_network[1] += -2
                            # else:
                            # b_network[1] += -2
                    selected = False

            update_display(WIN, grid, 8, WIDTH)
        pygame.time.delay(50)  # stops cpu dying
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        return w_network[1]

    board = [['  ' for i in range(8)] for j in range(8)]

    bp = Piece('b', 'p', 1, 'img/b_pawn.png')
    wp = Piece('w', 'p', 2, 'img/w_pawn.png')
    bk = Piece('b', 'k', 3, 'img/b_queen.png')
    wk = Piece('w', 'k', 4, 'img/w_queen.png')
    br = Piece('b', 'r', 5, 'img/b_rook.png')
    wr = Piece('w', 'r', 6, 'img/w_rook.png')
    bb = Piece('b', 'b', 7, 'img/b_bishop.png')
    wb = Piece('w', 'b', 8, 'img/w_bishop.png')
    bq = Piece('b', 'q', 9, 'img/b_king.png')
    wq = Piece('w', 'q', 10, 'img/w_king.png')
    bkn = Piece('b', 'kn', 11, 'img/b_knight.png')
    wkn = Piece('w', 'kn', 12, 'img/w_knight.png')

    starting_order = {(0, 0): pygame.image.load(br.image), (1, 0): pygame.image.load(bkn.image),
                      (2, 0): pygame.image.load(bb.image), (3, 0): pygame.image.load(bk.image),
                      (4, 0): pygame.image.load(bq.image), (5, 0): pygame.image.load(bb.image),
                      (6, 0): pygame.image.load(bkn.image), (7, 0): pygame.image.load(br.image),
                      (0, 1): pygame.image.load(bp.image), (1, 1): pygame.image.load(bp.image),
                      (2, 1): pygame.image.load(bp.image), (3, 1): pygame.image.load(bp.image),
                      (4, 1): pygame.image.load(bp.image), (5, 1): pygame.image.load(bp.image),
                      (6, 1): pygame.image.load(bp.image), (7, 1): pygame.image.load(bp.image),

                      (0, 2): None, (1, 2): None, (2, 2): None, (3, 2): None,
                      (4, 2): None, (5, 2): None, (6, 2): None, (7, 2): None,
                      (0, 3): None, (1, 3): None, (2, 3): None, (3, 3): None,
                      (4, 3): None, (5, 3): None, (6, 3): None, (7, 3): None,
                      (0, 4): None, (1, 4): None, (2, 4): None, (3, 4): None,
                      (4, 4): None, (5, 4): None, (6, 4): None, (7, 4): None,
                      (0, 5): None, (1, 5): None, (2, 5): None, (3, 5): None,
                      (4, 5): None, (5, 5): None, (6, 5): None, (7, 5): None,

                      (0, 6): pygame.image.load(wp.image), (1, 6): pygame.image.load(wp.image),
                      (2, 6): pygame.image.load(wp.image), (3, 6): pygame.image.load(wp.image),
                      (4, 6): pygame.image.load(wp.image), (5, 6): pygame.image.load(wp.image),
                      (6, 6): pygame.image.load(wp.image), (7, 6): pygame.image.load(wp.image),
                      (0, 7): pygame.image.load(wr.image), (1, 7): pygame.image.load(wkn.image),
                      (2, 7): pygame.image.load(wb.image), (3, 7): pygame.image.load(wk.image),
                      (4, 7): pygame.image.load(wq.image), (5, 7): pygame.image.load(wb.image),
                      (6, 7): pygame.image.load(wkn.image), (7, 7): pygame.image.load(wr.image), }

    WIDTH = 800

    WIN = pygame.display.set_mode((WIDTH, WIDTH))

    pygame.display.set_caption("Chess")
    WHITE = (180, 165, 255)
    GREY = (45, 0, 180)
    BLUE = (150, 200, 200)
    BLACK = (0, 0, 0)

    create_board(board)

    return main(WIN, WIDTH, network)