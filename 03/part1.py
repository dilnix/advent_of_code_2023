import re


def get_input() -> list[str]:
    """
    Reads the input file and returns a list of strings.
    """
    with open("input", "r") as f:
        return f.read().splitlines()


def get_adjacent_coordinates(coordinate):
    """
    Returns a list of adjacent coordinates to the given coordinate.

    Args:
        coordinate (tuple): The coordinate (x, y) for which to find adjacent coordinates.

    Returns:
        list: A list of adjacent coordinates.
    """
    x, y = coordinate
    return [(x+i, y+j) for i in range(-1, 2) for j in range(-1, 2) if not (i == 0 and j == 0)]


def is_adjacent_to_node(input_list, coordinate) -> bool:
    """
    Checks if the given coordinate is adjacent to a node in the input list.

    Args:
        input_list (list): The input list containing nodes.
        coordinate (tuple): The coordinate to check adjacency for.

    Returns:
        bool: True if the coordinate is adjacent to a node, False otherwise.
    """
    node_pattern = re.compile(r'[@#$%&*+=/-]')
    adjacent_coordinates = get_adjacent_coordinates(coordinate)
    for adj_coordinate in adjacent_coordinates:
        if (0 <= adj_coordinate[0] < len(input_list) and
            0 <= adj_coordinate[1] < len(input_list[adj_coordinate[0]]) and
                node_pattern.match(input_list[adj_coordinate[0]][adj_coordinate[1]])):
            return True
    return False


def process_input(input_list):
    """
    Process the input list and find connected part numbers.

    Args:
        input_list (list): List of strings representing the input.

    Returns:
        list: List of connected part numbers.
    """
    part_number_pattern: re.Pattern[str] = re.compile(r'\b\d{1,3}\b')
    connected_part_numbers = []
    for i, line in enumerate(input_list):
        for match in part_number_pattern.finditer(line):
            start, end = match.span()
            for j in range(start, end):
                if is_adjacent_to_node(input_list, (i, j)):
                    connected_part_numbers.append(int(match.group()))
                    break
    return connected_part_numbers


if __name__ == "__main__":
    input_list: list[str] = get_input()
    connected_part_numbers = process_input(input_list)
    # print(connected_part_numbers)
    print(sum(connected_part_numbers))
