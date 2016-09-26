Minesweeper Game - Python3
==========================

Widgets Structure
-----------------

- root window
	- top frame
		- bombs counter
		- new game button
		- options button => options window
		- help button => help window
		- timer
	- game frame
		- squares of the game (= frames)
			- button
- options window
- help window

In MVC model :
--------------
- *Model* = functions and data of the project
- *View* = display model to the user
- *Controller* = handle user input

- classes.py = *Model* : define structures of background board
- gui.py = *View* : create and bind graphical elements
- handlers.py = *Controller* : get click events and process them

- main.py : create GUI, initialise background data and call mainloop
- global_vars.py : contains global variables used everywhere
	(ok, a bit dirty but by far the easiest way to share variables)
- utils.py : various useful functions
