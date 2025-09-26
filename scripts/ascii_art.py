# A central repository for ASCII art used in the game.

# Simple, single-tile art.
PLAYER = '@'
ROCK = 'o'
BUSH = '*'
WALL = '#'
EMPTY = ' '
WATER = '~'

# More complex structures are defined as dictionaries of multi-line strings.
# The map generator can then pick from these to place larger features.

BUILDINGS = {
    "small_house": [
        " /\\ ",
        "/__\\"
    ],
    "shop": [
        "+----+",
        "|SHOP|",
        "+----+"
    ],
}

NATURE = {
    "pine_tree": [
        " /\\ ",
        "//\\\\"
    ],
    "rocks_cluster": [
        " o",
        "o o"
    ],
}

PEOPLE = {
    "villager": "i"
}

# This block allows for testing and previewing the art assets.
if __name__ == '__main__':
    print("--- Displaying ASCII Art Assets ---")

    print("\n[+] Simple Tiles:")
    print(f"  Player: {PLAYER}")
    print(f"  Rock:   {ROCK}")
    print(f"  Bush:   {BUSH}")
    print(f"  Wall:   {WALL}")

    print("\n[+] Buildings:")
    for name, art_lines in BUILDINGS.items():
        print(f"--- {name} ---")
        for line in art_lines:
            print(f"  {line}")

    print("\n[+] Nature:")
    for name, art_lines in NATURE.items():
        print(f"--- {name} ---")
        for line in art_lines:
            print(f"  {line}")

    print("\n[+] People:")
    for name, art in PEOPLE.items():
        print(f"--- {name} ---")
        print(f"  {art}")