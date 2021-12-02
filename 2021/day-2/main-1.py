from typing import List, Tuple
import os


DATA_FILENAME = 'data.txt'

def get_input(fake: bool) -> List[int]:
    if fake:
        return [
            'forward 5',
            'down 5',
            'forward 8',
            'up 3',
            'down 8',
            'forward 2',
        ]
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), DATA_FILENAME)) as f:
        return list(f.readlines())

def compute(input: List[str]) -> Tuple[int]:
    x, y = 0, 0
    for instruction in input:
        parts = instruction.split(' ')
        direction = parts[0]
        value = int(parts[1])
        if direction == 'forward':
            x += value
        elif direction == 'up':
            y -= value
        elif direction == 'down':
            y += value
    return (x, y)

if __name__ == "__main__":
    input = get_input(fake=False)
    x, y = compute(input)
    print(x * y)
