"""
Scratchcards 2.
Each line in the input file contains a scratchcard. First part of the line is the card number, before the colon,
like "Card 143:" or "Card   5:".
The second part, before the pipe, sontains 10 winning numbers, like: " 21  42  13  54  52  16  74  82   9 19 |".
The third part, after the pipe, contains 25 numbers scratched off that you have,
like: "| 30 37  2 15 24 49 19 86 62 70 60 88 79 11  1 98 71 55 14 48 51 35 23 16 96".
But there's no such thing as "points". Instead, scratchcards only cause you to win more
scratchcards equal to the number of winning numbers you have.
Specifically, you win copies of the scratchcards below the winning card equal to the
number of matches. So, if card 10 were to have 5 matching numbers, you would win one
copy each of cards 11, 12, 13, 14, and 15.
Copies of scratchcards are scored like normal scratchcards and have the same card
number as the card they copied. So, if you win a copy of card 10 and it has 5 matching
numbers, it would then win a copy of the same cards that the original card 10 won:
cards 11, 12, 13, 14, and 15. This process repeats until none of the copies cause you
to win any more cards. (Cards will never make you copy a card past the end of the table.)
Once all of the originals and copies have been processed until no more scratchcards are won,
you need to calculate the total number of scratchcards you have in the end.
"""

import re
from collections import defaultdict
from typing import DefaultDict, Set
from typing import Callable


class Scratchcard:
    """
    Scratchcard class.
    """

    def __init__(self, card_number: str, winning_numbers: Set[str], scratched_numbers: Set[str]) -> None:
        """
        Constructor.
        """
        self.card_number = card_number
        self.winning_numbers = winning_numbers
        self.scratched_numbers = scratched_numbers
        self.count = 0

        return None

    def __repr__(self) -> str:
        """
        String representation.
        """
        return f"Scratchcard {self.card_number} has {self.count} copies."

    def __str__(self) -> str:
        """
        String representation.
        """
        return self.__repr__()


def main() -> None:
    """
    Main function.
    """
    with open("input") as file:
        lines: list[str] = file.readlines()

    # Create a dictionary of scratchcards, keyed by card number.
    scratchcards: DefaultDict[str, Scratchcard] = defaultdict(
        # Provide a default factory function
        lambda: Scratchcard("", set(), set()))

    for line in lines:
        # Extract the card number and the winning numbers.
        card_number, winning_numbers = re.match(
            r"Card\s+(\d+):\s+([0-9\s]+)\s+\|", line).groups()
        winning_numbers = set(winning_numbers.split())

        # Extract the scratched numbers.
        scratched_numbers = re.search(r"\|\s+([0-9\s]+)$", line).group(1)
        scratched_numbers = set(scratched_numbers.split())

        # Add the card to the dictionary.
        scratchcards[card_number] = Scratchcard(
            card_number, winning_numbers, scratched_numbers)

    # Process the scratchcards.
    scratchcards = process_scratchcards(scratchcards)

    # Count the number of scratchcards.
    total = 0
    for card in scratchcards.values():
        total += card.count

    print(f"Total scratchcards: {total}")

    return None


def process_scratchcards(scratchcards: DefaultDict[str, Scratchcard]) -> DefaultDict[str, Scratchcard]:
    """
    Process the scratchcards.
    """
    # Create a set of cards to process.
    cards_to_process: Set[str] = set(scratchcards.keys())

    # Process the cards.
    while cards_to_process:
        # Get the next card to process.
        card_number = cards_to_process.pop()
        card = scratchcards[card_number]

        # Process the card.
        scratchcards = process_scratchcard(scratchcards, card)

    return scratchcards


def process_scratchcard(scratchcards: DefaultDict[str, Scratchcard], card: Scratchcard) -> DefaultDict[str, Scratchcard]:
    """
    Process a single scratchcard.
    """
    # Process the card.
    for number in card.scratched_numbers:
        if number in card.winning_numbers:
            # This card is a winner.
            card.count += 1

            # Create a copy of the card.
            copy = Scratchcard(card.card_number, card.winning_numbers,
                               card.scratched_numbers)

            # Add the copy to the dictionary.
            scratchcards[copy.card_number] = copy

    return scratchcards


if __name__ == "__main__":
    main()
