Minesweeper Game - Python3
==========================

Widgets Structure
-----------------

- root window
	- menu
	- top frame
		- bombs counter
		- timer
	- game frame
		- squares of the game (= frame)
			- button


Handling events procedure
-------------------------
- Click on a button => calls left or right handler with his pos
Handler executes actions depending on the button's/state and the click :
- Right click :
	- add/remove flag
	- increase/decrease number of bombs
- Left click :
	- discover
	- if bomb, loose
	- else if 0, discover neighbours
	


TODO
----

- package for global variables ? Would save parameters
- end game properly (win and loose)
- count and print numbers of bombs
- add parameters for size / number of bombs
- cf incator of difficulty 3BV


Still a bug in dependencies !
main need classes to generate a grid of squares
classes need to call an event handler, which have to access the grid of squares
