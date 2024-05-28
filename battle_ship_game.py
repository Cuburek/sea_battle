import field as fld
import random
import string


class BattleshipGame:
    def __init__(self, size: int, ships: int):
        self.size = size
        self.ships = ships
        self.player_field = fld.Field(self.size, self.ships)
        self.computer_field = fld.Field(self.size, self.ships)

    # Это функция расстановки кораблей, она уже полностью написана
    def place_ships_randomly(self, field, num_ships):
        for _ in range(num_ships):
            placed = False
            while not placed:
            
                coords = (random.randint(0, self.size - 1), random.randint(0, self.size - 1))
                if self.is_valid_ship_placement(field, coords):
                    field.grid[coords[0]][coords[1]] = fld.SHIP
                    placed = True

    # Это функция проверки расстановки кораблей, она уже полностью написана
    def is_valid_ship_placement(self, field, coords):
        x, y = coords

        # Проверка на наличие соседних клеток по горизонтали и вертикали
        for j in range(-1, 2):
            for k in range(-1, 2):
                new_x, new_y = x + j, y + k
                if 0 <= new_x < self.size and 0 <= new_y < self.size and field.grid[new_x][new_y] == fld.SHIP:
                    return False

        return True

    def play(self):
        self.place_ships_randomly(self.computer_field, self.ships)
        self.place_ships_randomly(self.player_field, self.ships)
        while True:
            self.display_fields()
            x, y = self.player_input()
            self.player_turn(x, y)
            if self.computer_field.ships_alive == 0:
                print("Вы победили! Все корабли компьютера потоплены")
                break

            self.computer_turn()
            if self.player_field.ships_alive == 0:
                print("Вы проиграли! Все ваши корабли потоплены")
                break

    def player_turn(self, x: str, y: int):
        x = string.ascii_uppercase.index(x)
        y -= 1
        if self.computer_field.grid[y][x] == fld.SHIP:
            print(f"Вы попали, стреляя по {string.ascii_uppercase[x]}{y + 1}!")
            self.computer_field.grid[y][x] = fld.DESTROYED_SHIP
            self.computer_field.ships_alive -= 1

        else:
            print(f"Вы промахнулись, стреляя по {string.ascii_uppercase[x]}{y + 1}.")
            self.computer_field.grid[y][x] = fld.MISS

    def computer_turn(self):
        x = random.randint(0, self.size - 1)
        y = random.randint(0, self.size - 1)

        if self.player_field.grid[y][x] == fld.SHIP:
            print(f"Компьютер попал по {string.ascii_uppercase[x]}{y + 1}")
            self.player_field.grid[y][x] = fld.DESTROYED_SHIP
            self.player_field.ships_alive -= 1

        else:
            print(f"Компьютер промахнулся, стреляя по {string.ascii_uppercase[x]}{y + 1}")
            self.player_field.grid[y][x] = fld.MISS

    def display_fields(self, show_ships_computer: bool = False):
        print("Расстановка кораблей компьютера:")
        self.computer_field.display()

        print("Ваша расстановка кораблей:")
        self.player_field.display(True)

    def player_input(self) -> tuple[str, int]:
        while True:
            x = input("Введи координату по горизонтали: ").strip().upper()
            try:
                y = int(input("Введите координату по вертикали: "))
            except ValueError:
                print("Координата по вертикали должна быть целым числом!")
                continue
            if x not in string.ascii_uppercase[:self.size] or len(x) != 1:
                print(f"Координата по горизонтали должна быть буквой в диапазоне от А до "
                      f"{string.ascii_uppercase[self.size - 1]} включительно")
            elif not 0 < y <= self.size:
                print(f"Координата по вертикали должна быть от 1 до {self.size} включительно")
            elif self.computer_field.grid[y - 1][string.ascii_uppercase.index(x)] == fld.DESTROYED_SHIP:
                print("Вы не можете стрелять в подбитый корабль")
            elif self.computer_field.grid[y - 1][string.ascii_uppercase.index(x)] == fld.MISS:
                print("Вы уже стреляли по этой клетке")

            else:
                return x, y
