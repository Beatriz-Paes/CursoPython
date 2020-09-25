# Enum
from enum import Enum, auto


class Direction(Enum):
    # right = 0
    # left = 1
    # up = 2
    # down = 3
    right = auto()
    left = auto()
    up = auto()
    down = auto()


def move(direction):
    # if direction != 'right' and direction != 'left':
    #     raise ValueError('Cannot move in this direction')

    if not isinstance(direction, Direction):
        raise ValueError('Cannot move in this direction')

    return f'Moving {direction.name}'


if __name__ == "__main__":
    # Conjunto de opções
    # print(move('right'))
    # print(move('left'))
    # print(move('up'))
    # print(move('down'))

    print(move(Direction.right))
    print(move(Direction.left))
    print(move(Direction.up))
    print(move(Direction.down))
    # print(move('Outra coisa'))

    for direction in Direction:
        print(direction, direction.value, direction.name)
