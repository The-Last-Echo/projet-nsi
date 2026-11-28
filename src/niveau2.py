import curses
import time
import random
import csv
import levels


current_level = 1
game_map = levels.levels[current_level]
frames_between_shots = 4


def save(map: list):
	with open("./save/save_map.csv", "w", newline="") as csvfile:
		writer = csv.writer(csvfile)

		writer.writerows(map)


def load_last_save() -> list:
	with open("./save/save_map.csv", newline="") as csvfile:
		reader = csv.reader(csvfile)
		map = []
		for row in reader:
			map.append(row)
		return map


def get_player_position(game_map): #find the player position on the map
    for y in range(len(game_map)):
        for x in range(len(game_map[y])):
            if game_map[y][x] == " P ":
                return (x, y)
    return None


def get_enemy_positions(game_map): #find all enemy positions on the map
    enemies = []

    for y in range(len(game_map)):
        for x in range(len(game_map[y])):
            if game_map[y][x] == " E ":
                enemies.append((x, y))

    return enemies


def get_new_pos(game_map, x, y, direction): #return the block in the direction of the player
    if direction == "up":
        y -= 1
    elif direction == "right":
        x += 1
    elif direction == "down":
        y += 1
    elif direction == "left":
        x -= 1

    return (x, y)


def check_new_pos(map, new_pos): #check what happens when the player touches a block
    tile = map[new_pos[1]][new_pos[0]]

    if tile == " . ":
        return "empty"
    elif tile == " E ":
        return "ennemy"
    elif tile == " P ":
    	return "player"
    elif tile == " W ":
        return "win"

    return "blocked"


def move_enemies(game_map): #move all enemies randomly or attack the player
    enemies = get_enemy_positions(game_map)

    for enemy_number in range(len(enemies)):
        x = enemies[enemy_number][0]
        y = enemies[enemy_number][1]

        #check if an enemy sees the player
        if game_map[y][x-1] == " P ":
           	return True
        elif game_map[y][x+1] == " P ":
           	return True
        elif game_map[y-1][x] == " P ":
           	return True
        elif game_map[y+1][x] == " P ":
            return True

        #choose a random direction
        directions = ["up", "right", "down", "left"]
        direction = random.choice(directions)

        new_pos = get_new_pos(game_map, x, y, direction)

        #move the enemy if the block is empty
        if check_new_pos(game_map, new_pos) == "empty":
            game_map[y][x] = " . "
            game_map[new_pos[1]][new_pos[0]] = " E "

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
    stats += " | " + status
    stdscr.addstr(1, 0, stats)

    #display the map
    for y in range(len(game_map)):
        line = ""

        for x in range(len(game_map[y])):
            line += game_map[y][x]

        stdscr.addstr(y + 2, 0, line)

    stdscr.refresh()


def game(stdscr):
    global game_map

    player_pos = get_player_position(game_map)

    stdscr.keypad(True)
    stdscr.timeout(100)

    status = ""
    refresh(stdscr, game_map, status)

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

        if direction:

            #move the player
            player_pos = get_player_position(game_map)

            player_pos_x = player_pos[0]
            player_pos_y = player_pos[1]

            new_pos = get_new_pos(game_map, player_pos_x, player_pos_y, direction)
            tile = check_new_pos(game_map, new_pos)

            if tile == "empty":
                game_map[player_pos_y][player_pos_x] = " . "
                game_map[new_pos[1]][new_pos[0]] = " P "
                status = ""

            elif tile == "ennemy":
                status = "You touched an enemy !"
                refresh(stdscr, game_map, status)
                time.sleep(1)
                break

            elif tile == "win":
                status = "You won !"
                refresh(stdscr, game_map, status)
                time.sleep(1)
                break

            refresh(stdscr, game_map, status)
            time.sleep(0.1) #time between player refresh and ennemy refresh

            #move enemies after the player moves
            game_over = move_enemies(game_map)

            if game_over:
                status = "An enemy attacks you !"
                refresh(stdscr, game_map, status)
                time.sleep(1)
                break

            refresh(stdscr, game_map, status)
            save(game_map)
            time.sleep(0) #The minimum time before player can act again (in seconds)


curses.wrapper(game)
