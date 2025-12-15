from core.parser import parse_line
from core.commands import move
import core.state as state

commands = [
    "MOVE 0 0 8 0",
    "MOVE 4 0 8 1",
    "MOVE 4 4 8 1"
]

for line in commands:
    command, params = parse_line(line)

    if command == "MOVE":
        ax, ay, bx, by = params
        state.current_x, state.current_y = move(ax, ay, bx, by)
