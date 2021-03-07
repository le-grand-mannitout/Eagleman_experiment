
import curses
import time

def main_menu(stdscr, reaction_time, variation, nb_tries_bf_change):

	k = 0
	nb_tries = 0

	curses.start_color()
	curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
	curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)

	while (k != ord('q')):
		stdscr.bkgd(" ", curses.color_pair(1))
        
		if k == 97:
			
			time.sleep(reaction_time)
			
			nb_tries = flash(stdscr, nb_tries)
			reaction_time = limit_tries(nb_tries_bf_change, reaction_time, nb_tries, variation)

		stdscr.refresh()
    
		k = stdscr.getch()


def flash(stdscr, nb_tries):
	
	stdscr.bkgd(" ", curses.color_pair(2))
	stdscr.refresh()
	time.sleep(1)
	stdscr.bkgd(" ", curses.color_pair(1))
	
	return (nb_tries + 1)
	
	
def limit_tries(nb_tries_bf_change, reaction_time, nb_tries, variation):
	
	if nb_tries == nb_tries_bf_change:
		reaction_time -= variation
		
	return reaction_time


def main():
    curses.wrapper(main_menu, 2, 2, 2)

if __name__ == "__main__":
    main()

