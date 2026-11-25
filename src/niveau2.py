
import curses
import time
import random
import csv
import levels


current_level = 1
game_map = levels.levels[current_level]


def save(map: list):
	with open("save.csv", "w", newline="") as csvfile:
		writer = csv.writer(csvfile)

		writer.writerows(map)


def load_last_save() -> list:
	with open("save.csv", newline="") as csvfile:
		reader = csv.reader(csvfile)
		map = []
		for row in reader:
			map.append(row)
		return map


def get_player_position(game_map): #find the player position on the map
    for y in range(len(game_map)):
        for x in range(len(game_map[y])):
            if game_map[y][x] == " P ":
                return [x, y]
    return None


def get_enemy_positions(game_map): #find all enemy positions on the map
    enemies = []

    for y in range(len(game_map)):
        for x in range(len(game_map[y])):
            if game_map[y][x] == " E ":
                enemies.append([x, y])

    return enemies


def get_block(game_map, x, y, direction): #return the block in the direction of the player
    if direction == "up":
        y -= 1
    elif direction == "right":
        x += 1
    elif direction == "down":
        y += 1
    elif direction == "left":
        x -= 1

    return game_map[y][x]


def get_block_type(block): #return the type of the block
    if block == " # ":
        return "wall"
    elif block == " . ":
        return "empty"
    elif block == " E ":
        return "enemy"
    elif block == " W ":
        return "win"

    return "unknown"


def check_block(block): #check what happens when the player touches a block
    block_type = get_block_type(block)

    if block_type == "wall":
        return "blocked"
    elif block_type == "empty":
        return "move"
    elif block_type == "enemy":
        return "error"
    elif block_type == "win":
        return "win"

    return "blocked"


def move_enemies(game_map): #move all enemies randomly or attack the player
    enemies = get_enemy_positions(game_map)

    for enemy_number in range(len(enemies)):
        x = enemies[enemy_number][0]
        y = enemies[enemy_number][1]

        #check if an enemy sees the player
        if game_map[y - 1][x] == " P ":
            return True
        elif game_map[y + 1][x] == " P ":
            return True
        elif game_map[y][x - 1] == " P ":
            return True
        elif game_map[y][x + 1] == " P ":
            return True

        #choose a random direction
        directions = ["up", "right", "down", "left"]
        direction = random.choice(directions)

        block = get_block(game_map, x, y, direction)

        #move the enemy if the block is empty
        if block == " . ":
            game_map[y][x] = " . "

            if direction == "up":
                y -= 1
            elif direction == "right":
                x += 1
            elif direction == "down":
                y += 1
            elif direction == "left":
                x -= 1

            game_map[y][x] = " E "

    return False


def refresh(stdscr, game_map, status): #refresh the screen with the current map
    stdscr.clear()

    #display the top border
    width = len(game_map[0])
    stdscr.addstr(0, 0, " # " * width)

    #display the statistics
    enemies = get_enemy_positions(game_map)
    stats = " # Level: " + str(current_level)
    stats += " | Enemies: " + str(len(enemies))

    #display the map
    for x in range(len(game_map)):
        line = ""

        for y in range(len(game_map[x])):
            line += game_map[x][y]

        stdscr.addstr(x + 2, 0, line)

    stdscr.refresh()


def game(stdscr):
    global game_map

    playerPosition = get_player_position(game_map)

    stdscr.keypad(True)
    stdscr.timeout(100)

    status = ""

    while True:
        key = stdscr.getch()

        if key == 27: #key code for escape
            break

        direction = None

        if key in [curses.KEY_UP, ord("z")]:
            direction = "up"
        elif key in [curses.KEY_RIGHT, ord("d")]:
            direction = "right"
        elif key in [curses.KEY_DOWN, ord("s")]:
            direction = "down"
        elif key in [curses.KEY_LEFT, ord("q")]:
            direction = "left"

        if direction != None:
            playerPosition = get_player_position(game_map)

            x = playerPosition[0]
            y = playerPosition[1]

            block = get_block(game_map, x, y, direction)
            action = check_block(block)

            if action == "move":
                game_map[y][x] = " . "

                if direction == "up":
                    y -= 1
                elif direction == "right":
                    x += 1
                elif direction == "down":
                    y += 1
                elif direction == "left":
                    x -= 1

                game_map[y][x] = " P "
                status = ""

                #move enemies after the player moves
                game_over = move_enemies(game_map)

                if game_over:
                    status = "An enemy attacks you!"
                    refresh(stdscr, game_map, status)
                    time.sleep(1)
                    break

            elif action == "error":
                status = "Error: You touched an enemy!"
                refresh(stdscr, game_map, status)
                time.sleep(1)
                break

            elif action == "win":
                status = "WIN! You won!"
                refresh(stdscr, game_map, status)
                time.sleep(1)
                break

            refresh(stdscr, game_map, status)
            save(game_map)
            time.sleep(0.1) #The minimum time before player can act again (in seconds)


curses.wrapper(game)
