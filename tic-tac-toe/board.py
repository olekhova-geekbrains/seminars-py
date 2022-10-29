BOARD_TEMPLATE = """
╔═══╤═══╤═══╗
║ * │ * │ * ║
╟───┼───┼───╢
║ * │ * │ * ║
╟───┼───┼───╢
║ * │ * │ * ║
╚═══╧═══╧═══╝
"""


def create_board(brd: list, board_template: str = BOARD_TEMPLATE, sym: str = '*') -> str:
    result = board_template
    for row in brd:
        for cell in row:
            result = result.replace(sym, cell, 1)
    return result