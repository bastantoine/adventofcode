from typing import Dict, List, Tuple
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

def filter_input(input: List[str], expected_value: str, position: int) -> List[str]:
    return [item for item in input if item[position] == expected_value][:]

def compute_freqs(input: List[str]) -> List[Dict[str, int]]:
    return [dict(Counter(''.join(item))) for item in list(zip(*input))][:]

def compute(input: List[str]) -> Tuple[int]:
    oxygen_generator_rating_inputs = input[:]
    for i in range(len(input)):
        freq = compute_freqs(oxygen_generator_rating_inputs)[i]
        if freq['0'] > freq['1']:
            oxygen_generator_rating_inputs = filter_input(oxygen_generator_rating_inputs, '0', i)
        else:
            oxygen_generator_rating_inputs = filter_input(oxygen_generator_rating_inputs, '1', i)
        if len(oxygen_generator_rating_inputs) == 1:
            break

    co2_scrubber_rating_inputs = input[:]
    for i in range(len(input)):
        freq = compute_freqs(co2_scrubber_rating_inputs)[i]
        if freq['0'] > freq['1']:
            co2_scrubber_rating_inputs = filter_input(co2_scrubber_rating_inputs, '1', i)
        else:
            co2_scrubber_rating_inputs = filter_input(co2_scrubber_rating_inputs, '0', i)
        if len(co2_scrubber_rating_inputs) == 1:
            break

    oxygen_generator_rating = oxygen_generator_rating_inputs[0]
    co2_scrubber_rating = co2_scrubber_rating_inputs[0]
    return int(oxygen_generator_rating, 2), int(co2_scrubber_rating, 2)

if __name__ == "__main__":
    input = get_input(fake=False)
    oxygen_generator_rating, co2_scrubber_rating = compute(input)
    print(oxygen_generator_rating * co2_scrubber_rating)
