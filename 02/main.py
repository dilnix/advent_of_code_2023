"""
There is an input file named "input". It contains a list of games and their details on each line.
Each game is numbered before colon and contains the different number of sets of color amounts
after colon that are used in the game. From 1 to 3 colors are possible in a set from proposed: red, green, blue.
The delimiter between those sets is a semicolon. The delimeter between colors in a set is a comma.
A single function named "main" should:
- read the file "input"
- parse it line by line
- get the number of the game, splitting the line by colon and removing the word "Game"
- get the number of each color in each set per game, splitting the line by semicolon and then by comma
- check which is the maximum number of each color across the sets per game and store it in a dictionary of maximums
- multiply together the values in the dictionary and append the result to a list of game powers
- compare the number of colors in each set per game with the default maximum possible number of colors in a set
- if the number of colors in a set is less or equal to the default maximum possible number of colors in a set, then
append the number of the game to the list of games passing the check
- return the sum of the numbers of the games passed and the sum of all the game powers as a string
"""


import math


DEFAULT_MAX_COLORS_IN_SET: dict[str, int] = {
    'red': 12,
    'green': 13,
    'blue': 14,
}


def main() -> str:
    games_passing = []
    powers = []
    with open('input', 'r') as f:
        for line in f:
            game_pass = True
            game, sets = line.split(': ')
            game = int(game.replace('Game ', ''))
            sets = sets.strip()
            sets = sets.split('; ')
            print(game, sets)
            game_max_colors = {}
            for set_ in sets:
                set_max_colors = {}
                colors = set_.split(', ')
                for color in colors:
                    amounts: list[int] = [int(amount) for amount in color.split(' ')
                                          if amount.isdigit()]
                    amount, color = color.split(' ')
                    set_max_colors.update({color: max(amounts)})
                    if int(amount) > DEFAULT_MAX_COLORS_IN_SET[color]:
                        game_pass = False
                for color, amount in set_max_colors.items():
                    if color not in game_max_colors:
                        game_max_colors.update({color: amount})
                    elif amount > game_max_colors[color]:
                        game_max_colors.update({color: amount})
            print(f"Game {game} max colors: {game_max_colors}")
            game_power: int = math.prod(game_max_colors.values())
            print(f"Game {game} power: {game_power}")
            powers.append(game_power)
            if game_pass:
                print(f'Game {game} passed')
                games_passing.append(int(game))
    return f"The sum of IDs is: {str(sum(games_passing))}. The sum of powers is: {str(sum(powers))}"


if __name__ == '__main__':
    print(main())
