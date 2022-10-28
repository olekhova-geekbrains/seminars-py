BOARD_TEMPLATE = """
╔═══╤═══╤═══╗
║ * │ * │ * ║
╟───┼───┼───╢
║ * │ * │ * ║
╟───┼───┼───╢
║ * │ * │ * ║
╚═══╧═══╧═══╝
"""


def create_board(brd: list) -> list:
    result = BOARD_TEMPLATE
    for row in brd:
        for cell in row:
            result = result.replace('*', cell, 1)
    return result
