import curses
from dbloader import loadGameData

rooms, player = loadGameData("data.json")

def main(screen):
    screen.keypad(True)

    maxY, maxX = screen.getmaxyx()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    while True:

        window1 = curses.newwin(round(maxY * .8), round(maxX * .6), 0, 0)
        window1.box()
        w1y, w1x = window1.getmaxyx()
        w1sy = (w1y // 2) - 1
        w1sx = ((w1x // 2) - len(player.currentRoom.name)) // 2
        window1.addstr(w1sy, w1sx, f"You're in the {player.currentRoom.name}", curses.A_BLINK | curses.color_pair(2))
        window1.addstr(w1sy + 1, w1sx, f"{player.currentRoom.description}", curses.color_pair(3))
        window1.addstr(w1sy + 3, w1sx, f"Exits from the room: " + ", ".join(player.currentRoom.exits.keys()), curses.color_pair(2))
        window1.addstr(w1sy + 5, w1sx, f"Items in the room: " + ", ".join(item.name for item in player.currentRoom.items), curses.color_pair(2))

        
        window2 = curses.newwin(round(maxY * .8), round(maxX * .4) , 0, round(maxX * .6))
        window2.box()
        w2y, w2x = window2.getmaxyx()
        w2sy = (w2y // 2) - 1
        window2.addstr(w2sy, 5, f"=======Inventory=======", curses.A_BLINK | curses.color_pair(1))
        window2.addstr(w2sy + 2, 5, ", ".join(item.name for item in player.inventory), curses.A_BLINK | curses.color_pair(3))
        
        
        window3 = curses.newwin(round(maxY * .2), maxX, round(maxY * .8), 0)
        window3.box()
        w3y, w3x = window3.getmaxyx()
        w3x = w3x // 2
        w3y = w3y // 2


        window1.refresh()
        window2.refresh()
        window3.refresh()

        window3.addstr(w3y, w3x, "Enter a string:")
        #window3.move(w3y + 1, w3x)
        command = window3.getstr().decode()

        if command == "quit":
            screen.keypad(False)
            curses.endwin()
            break
        elif command in player.currentRoom.exits:
            player.move(command, rooms)
        elif command.startswith("pick up "):
            item = command[8:]
            player.takeItem(item)
        elif command.startswith("drop "):
            item = command[5:]
            player.dropItem(item)


curses.wrapper(main)





