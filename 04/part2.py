"""
Scratchcards 2.
Each line in the input file contains a scratchcard and its details. Like a tower of scratchcards. First is on top.
First part of the line is the card number, before the colon, like "Card 143:" or "Card   5:".
The second part, after the colon but before the pipe symbol, sontains 10 winning numbers,
like: " 21  42  13  54  52  16  74  82   9 19 |".
The third part, after the pipe, contains 25 scratched off numbers for that card,
like: "| 30 37  2 15 24 49 19 86 62 70 60 88 79 11  1 98 71 55 14 48 51 35 23 16 96".
But surprise, there's no such thing as "points" that you win.
By winning a scratchcard, you're winning a number of copies of the scratchcard below it. The number of copies
is equal to the number of winning numbers you have.
For example, if card 10 had 5 matching numbers, you win a copy of each of cards: 11, 12, 13, 14, and 15.
Copies of scratchcards are scored like normal scratchcards and have the same card number as the card they copied.
So, if you win a copy of card 10 and it has 5 matching numbers, it would then win a copy of the same cards that
the original card 10 won: cards 11, 12, 13, 14, and 15.
This process repeats until none of the copies cause you to win any more cards.
Cards will never make you copy a card past the end of the tower.
Once all of the originals and copies have been processed until the bottom of the tower,
the task is to calculate the total number of scratchcards you have (original ones and all copies by winning them).

Action plan:
1. Parse the input file.
2. Create a dictionary to store the winning numbers for each card.
3. Create a dictionary to store the scratched numbers for each card.
4. Create a dictionary to store the number of copies of each card.
5. Create a dictionary to store the number of scratchcards you have.
6. Create a set to store the card numbers that have been processed.
7. Create a function to process a card and its copies.
8. Process the cards from top to bottom of the tower.
9. Calculate the total number of scratchcards you have.
10. Print the total number of scratchcards you have.
"""

import re
from typing import Dict, Set


def main() -> None:
    """
    Main function.
    """
    with open("input") as file:
        lines: list[str] = file.readlines()

    # Create a dictionary to store the winning numbers for each card.
    winning_numbers: Dict[int, Set[str]] = {}
    # Create a dictionary to store the scratched numbers for each card.
    scratched_numbers: Dict[int, Set[str]] = {}
    # Create a dictionary to store the number of copies of each card.
    copies: Dict[int, int] = {}
    # Create a dictionary to store the number of scratchcards you have.
    scratchcards: Dict[int, int] = {}
    # Create a set to store the card numbers that have been processed.
    processed: Set[int] = set()

    # Parse the input file.
    for line in lines:
        # Extract the card number and the winning numbers.
        card_number, winning_numbers_str = re.match(
            r"Card\s+(\d+):\s+([0-9\s]+)\s+\|", line).groups()
        winning_numbers[int(card_number)] = set(winning_numbers_str.split())

        # Extract the scratched numbers.
        scratched_numbers_str = re.search(r"\|\s+([0-9\s]+)$", line).group(1)
        scratched_numbers[int(card_number)] = set(scratched_numbers_str.split())

        # Initialize the number of copies and scratchcards.
        copies[int(card_number)] = 0
        scratchcards[int(card_number)] = 0

    # Create a function to process a card and its copies.
    def process_card(card_number: int) -> None:
        """
        Process a card and its copies.
        """
        # If the card has been processed, return.
        if card_number in processed:
            return None

        # Initialize the number of copies.
        copies[card_number] = len(winning_numbers[card_number] & scratched_numbers[card_number])

        # Process the copies.
        for i in range(1, copies[card_number] + 1):
            process_card(card_number + i)

        # Calculate the number of scratchcards you have.
        scratchcards[card_number] = 1 + sum(scratchcards[card_number + i] for i in range(1, copies[card_number] + 1))

        # Add the card to the set of processed cards.
        processed.add(card_number)

    # Process the cards from top to bottom of the tower.
    for card_number in sorted(winning_numbers.keys()):
        process_card(card_number)

    # Calculate the total number of scratchcards you have.
    total: int = sum(scratchcards.values())

    # Print the total number of scratchcards you have.
    print(f"Total number of scratchcards you have: {total}")

    return None


if __name__ == "__main__":
    main()
