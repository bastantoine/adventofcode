from typing import List, Tuple
import os
from collections import Counter


DATA_FILENAME = 'data.txt'

def get_input(fake: bool) -> List[int]:
    if fake:
        return [
            '00100',
            '11110',
            '10110',
            '10111',
            '10101',
            '01111',
            '00111',
            '11100',
            '10000',
            '11001',
            '00010',
            '01010',
        ]
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), DATA_FILENAME)) as f:
        return list(f.readlines())

def compute(input: List[str]) -> Tuple[int]:
    freqs = [dict(Counter(''.join(item))) for item in list(zip(*input))]
    gamma_rate, epsilon_rate = '', ''
    for freq in freqs:
        freq0 = freq['0']
        freq1 = freq['1']
        if freq0 > freq1:
            gamma_rate += '0'
            epsilon_rate += '1'
        else:
            gamma_rate += '1'
            epsilon_rate += '0'
    return int(gamma_rate, 2), int(epsilon_rate, 2)

if __name__ == "__main__":
    input = get_input(fake=False)
    gamma, epsilon = compute(input)
    print(gamma * epsilon)
