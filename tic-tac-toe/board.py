BOARD_TEMPLATE = """
╔═══╤═══╤═══╗
║ * │ * │ * ║
╟───┼───┼───╢
║ * │ * │ * ║
╟───┼───┼───╢
║ * │ * │ * ║
╚═══╧═══╧═══╝
"""


def create_board(brd: list, board_template: str = BOARD_TEMPLATE) -> list:
    result = board_template
    for row in brd:
        for cell in row:
            result = result.replace('*', cell, 1)
    return result
