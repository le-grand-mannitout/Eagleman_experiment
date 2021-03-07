
import curses

def main_menu(stdscr, initial_reaction, variation, nb_of_tries_bf_change):

    k = 0

    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)

    while (k != ord('q')):

        if k == 97:
            stdscr.bkgd(" ", curses.color_pair(2))

        stdscr.refresh()
    
        k = stdscr.getch()


def main():
    curses.wrapper(main_menu)

if __name__ == "__main__":
    main()

