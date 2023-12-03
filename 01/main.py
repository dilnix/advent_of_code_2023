"""
The single function in this module will read each line from the file
called "input", parse each line searching for digits (natural or literal),
calculate the value built from combining the two digits (first occurrence
and last one, even if it's the same) of each line, and then return the
sum of all.
Each line contains at least 1 digit among alphabetical characters, and
may contain or not contain literal digits as well.
"""

import re


# mapping of literal digits to their corresponding natural digits
MAPPING: dict[str, str] = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}


# function to parse each line and calculate the value
def main() -> int:
    with open('input') as f:
        total: int = 0
        for line in f:
            print(line.strip())
            # create a combined list of natural and literal digits
            digits_list: list[str] = list(
                MAPPING.keys()) + list(MAPPING.values())
            # join the items in this list into a regular expression pattern
            pattern: str = r'(?=(' + '|'.join(digits_list) + r'))'
            # find all the digits (natural or literal) in the order they appear in the line
            matches: list[str] = re.findall(pattern, line)
            print(matches)
            if matches:
                # select the first and last match
                selected_matches: list[str] = [matches[0], matches[-1]]
                print(selected_matches)
                # convert selected matches to natural digits
                digits: list[str] = [MAPPING.get(
                    match, match) for match in selected_matches]
                print(digits)
                # concatenate the selected digits
                value: int = int(''.join(digits))
                print(value)
                # add the value to the sum
                total += value
    return total


if __name__ == '__main__':
    print('\n', main())
