import string

SHIP = "🚢"
EMPTY = "🟦"
MISS = "🟥"
DESTROYED_SHIP = "🛑"


class Field:
    def __init__(self, size, ships):
        self.size = size
        self.ships = ships
        self.ships_alive = ships
        self.grid = []
        for _ in range(size):
            row = []
            for _ in range(size):
                row.append(None)
            self.grid.append(row)

    def display(self, show_ships=False):
        letters = string.ascii_uppercase
        letters1 = "   " + "┄┄".join(letters[:self.size])
        print(letters1)

        output_shift = len(str(len(self.grid)))

        for i in range(self.size):
            print('{:{shift}}'.format(i + 1, shift=output_shift), end=' ')
            for j in range(self.size):
                if self.grid[i][j] == SHIP and show_ships:
                    print(SHIP, end=" ")
                elif self.grid[i][j] is not None:
                    print(self.grid[i][j], end=" ")
                else:
                    print(EMPTY, end=" ")
            print()

