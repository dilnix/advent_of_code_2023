import re
from part1 import get_input
from part1 import get_adjacent_coordinates


def get_adjacent_part_numbers(input_list, coordinate):
    part_number_pattern: re.Pattern[str] = re.compile(r'\b\d{1,3}\b')
    adjacent_part_numbers = []
    for i, line in enumerate(input_list):
        for match in part_number_pattern.finditer(line):
            start, end = match.span()
            for j in range(start, end):
                if coordinate in get_adjacent_coordinates((i, j)):
                    adjacent_part_numbers.append(int(match.group()))
                    break
    return adjacent_part_numbers


def process_input(input_list):
    gear_pattern: re.Pattern[str] = re.compile(r'\*')
    multiplied_part_numbers = []
    for i, line in enumerate(input_list):
        for match in gear_pattern.finditer(line):
            start, end = match.span()
            for j in range(start, end):
                adjacent_part_numbers = get_adjacent_part_numbers(
                    input_list, (i, j))
                if len(adjacent_part_numbers) == 2:
                    multiplied_part_numbers.append(
                        adjacent_part_numbers[0] * adjacent_part_numbers[1])
    return multiplied_part_numbers


if __name__ == "__main__":
    input_list: list[str] = get_input()
    multiplied_part_numbers = process_input(input_list)
    # print(multiplied_part_numbers)
    print(sum(multiplied_part_numbers))
