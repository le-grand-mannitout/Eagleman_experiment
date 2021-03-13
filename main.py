
import curses
import time

from config import Config


KEY_A = 97
KEY_ENTER = 10
KEY_SPACE = 32

def main_menu(stdscr,
              reaction_time: float,
              variation: float,
              nb_tries_bf_change: int):
    """
        Main curses menu that gets user input
    """
    curses.curs_set(0)
    k = 0
    nb_tries = 0

    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)

    while k != ord("q"):
        stdscr.bkgd(" ", curses.color_pair(1))

        if k in (KEY_A, KEY_ENTER, KEY_SPACE):
            time.sleep(reaction_time)

            nb_tries = flash(stdscr, nb_tries, Config.flash_time)
            reaction_time = limit_tries(nb_tries_bf_change,
                                        reaction_time,
                                        nb_tries, variation)

        stdscr.refresh()
        k = stdscr.getch()


def flash(stdscr,
          nb_tries: int,
          flash_time: float) -> int:
    """
        White flash appears on screen
    """
    stdscr.bkgd(" ", curses.color_pair(2))
    stdscr.refresh()
    time.sleep(flash_time)
    stdscr.bkgd(" ", curses.color_pair(1))

    return nb_tries + 1


def limit_tries(nb_tries_bf_change: int,
                reaction_time: float,
                nb_tries: int,
                variation: float) -> float:
    """
        Determine if limit of first time sequence is reach and
        adapt reaction time if this is the case
    """
    if nb_tries == nb_tries_bf_change:
        reaction_time -= variation

    return reaction_time


def main():
    curses.wrapper(main_menu,
                   Config.reaction_time,
                   Config.variation,
                   Config.nb_tries_bf_change)


if __name__ == "__main__":
    main()
