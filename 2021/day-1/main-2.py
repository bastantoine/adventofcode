from typing import Dict, List
import os


DATA_FILENAME = 'data.txt'

def get_input(fake: bool) -> List[int]:
    if fake:
        return [199,200,208,210,200,207,240,269,260,263]
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), DATA_FILENAME)) as f:
        return [int(v) for v in f.readlines()]

def compute_windows(input: List[int]) -> List[int]:
    return [sum(input[i:i+3]) for i in range(len(input) - 2)]

def compute(input: List[int]) -> int:
    nb_increase = 0
    previous_value = -1
    for value in input:
        if previous_value != -1 and value > previous_value:
            nb_increase += 1
        previous_value = value
    return nb_increase


if __name__ == "__main__":
    input = get_input(fake=False)
    input = compute_windows(input)
    print(compute(input))
