"""
Scratchcards.
Each line in the input file contains a scratchcard. First part of the line is the card number, before the colon,
like "Card 143:" or "Card   5:".
The second part, before the pipe, sontains 10 winning numbers, like: " 21  42  13  54  52  16  74  82   9 19 |".
The third part, after the pipe, contains 25 numbers scratched off that you have,
like: "| 30 37  2 15 24 49 19 86 62 70 60 88 79 11  1 98 71 55 14 48 51 35 23 16 96".
The task is to figure out which of the numbers you have appear in the list of winning numbers. The first match makes
the card worth one point and each match after the first doubles the point value of that card.
How many points are they worth in total?
"""

import re


def main() -> None:
    """
    Main function.
    """
    with open("input") as file:
        lines: list[str] = file.readlines()

    total = 0
    for line in lines:
        # Extract the card number and the winning numbers.
        card_number, winning_numbers = re.match(
            r"Card\s+(\d+):\s+([0-9\s]+)\s+\|", line).groups()
        winning_numbers = set(winning_numbers.split())

        # Extract the scratched numbers.
        scratched_numbers = re.search(r"\|\s+([0-9\s]+)$", line).group(1)
        scratched_numbers = set(scratched_numbers.split())

        # Calculate the points.
        points = 0
        for number in scratched_numbers:
            if number in winning_numbers:
                if points == 0:
                    points += 1
                    winning_numbers.remove(number)
                else:
                    points *= 2
                    winning_numbers.remove(number)
        total += points

        print(f"Card {card_number} is worth {points} points.")

    print(f"Total points: {total}")

    return None


if __name__ == "__main__":
    main()
