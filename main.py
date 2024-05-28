from field import Field
from field import SHIP, MISS, EMPTY, DESTROYED_SHIP
from battle_ship_game import BattleshipGame

size = 0
ships = 0
while True:
    try:
        size = int(input("Введите размер поля. Это должно быть целое число. Размер: "))
    except ValueError:
        print("Пожалуйста, введите целое число.")
        continue

    if not 0 < size <= 26:
        print("Размер поля должен находиться в диапазоне от 1 до 26")
        continue
    break

min_ships, max_ships = size ** 2 // 9, size ** 2 // 6

while True:
    try:
        ships = int(input(f"Введите количество кораблей. Это должно быть целое число."
                          f"Рекомендуемое количество кораблей от {min_ships} до {max_ships}"
                          f"При выборе значения >{max_ships} возможно зависание игры. Количество кораблей: "))
    except ValueError:
        print("Пожалуйста, введите целое число.")
        continue

    if ships <= 0:
        print("Количество кораблей не должно быть меньше 1 единицы")
        continue
    break


battle_ship = BattleshipGame(size, ships)
battle_ship.play()
# battle_ship.player_input()
# field.grid[0][1] = SHIP
# field.grid[2][1] = MISS
# field.grid[1][1] = DESTROYED_SHIP

