import random

from how_to_think.chapter_14.section_14_3_draw_queens import draw_board


def share_diagonal(x0, y0, x1, y1):
    """ Is (x0, y) on the same shared diagonal with (x1, y1)? """
    dx = abs(x1 - x0)  # Calc the absolute y distance
    dy = abs(y1 - y0)  # Calc the absolute x distance
    return dx == dy  # They clash if dx == yx


def col_clashes(bs, c):
    """ Return True if the queen at column c clashes
        with any queen to its left.
    """
    for i in range(c):  # Look at all columns to the left of c
        if share_diagonal(i, bs[i], c, bs[c]):
            return True
    return False  # No clashes - col c has a safe placement


def has_clashes(the_board):
    """ Determine whether we have any queens clashing on the diagonal.
        We're assuming here that the_board is a permutation of column
        numbers, so we're not explicitly checking row or column clashes.
    """
    for col in range(1, len(the_board)):
        if col_clashes(the_board, col):
            return True
    return False


def find_queen_problem_solutions():
    board = list(range(8))
    num_found = 0
    tries = 0
    while num_found < 10:
        random.shuffle(board)
        tries += 1
        if not has_clashes(board):
            draw_board(board)
            num_found += 1


if __name__ == '__main__':
    find_queen_problem_solutions()
