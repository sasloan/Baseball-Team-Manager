# Baseball-Team-Manager

A project to manage a baseball team’s information
(1)	Create a program that lets the manager of a sports team track the data for each player and  display the lineup for the upcoming first game of the season and any subsequent games. 
(2)	Store the data in a text file that is loaded when the program starts. 
Sample Console Output
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                Baseball Team Management Program
MENU OPTIONS
1 – Display lineup
2 – Add player
3 – Remove player
4 – Move player
5 – Edit player position
6 – Edit player stats
7 - Exit program

POSITIONS
C, 1B, 2B, 3B, SS, LF, CF, RF, P
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Menu option: 2
Name: Mike
Position: c
At bats: 11
Hits: 4
Mike was added.

Menu option: 1
	Player		POS	AB	H	AVG
----------------------------------------------------------------
1	Trevor		SS	588	173	0.294
2	Garrett	2B	299	74	0.247
3	Tony		C	535	176	0.329
4	Hunter		RF	580	182	0.314
5	Ian		CF	443	113	0.255
6	Nolan		3B	588	185	0.315
7	Daniel		1B	430	129	0.3
8	David		LF	374	113	0.302
9	Phillip	P	102	12	0.118

Menu option: 3
Enter a lineup number to remove: 10
Mike was deleted.

Menu option: 4
Enter a current lineup number to move: 8
Jarrett was selected.
Enter a new lineup number: 2
Jarrett was moved.

Menu option: 5
Enter a lineup number to edit: 1
You selected Joe: Position=2B
Enter a new Position: SS
Joe was updated.

Menu option: 7
Bye!

Specifications
PART 1
•	Create a program that manages a team by storing data in a list of players. The module with the main method will be named Presentation_XYZ.py (replace XYZ with your initials). The list will be stored in the main method.
•	Use a list of lists to store each player in the lineup. The list for a single player includes their name, position, at bats, and hits. This is the ‘inner’ list.
aPlayerListVariable = ['Trevor', 'SS', '588', '173'],

The list of player lists is the ‘outer’ list. 
aLineupListVariable = [['Trevor', 'SS', '588', '173'], 
                                              ['Garrett', '2B', '299', '74']]
•	For part 1 this list will be declared with a statement in the main method.
•	Use functions to organize the code making it reusable, easy to read, and easy to maintain. Each of the functions for the six main menu features should take the list of players as an input parameter. 
•	Use a tuple to store all valid positions (‘C’, ‘1B’, ‘2B’, etc).
•	When entering/editing positions, the program should always require the user to enter a valid position. 
•	The formula for calculating batting average is:
average = hits / at_bats
•	The program should round batting average to a maximum of three decimal places.
•	If the user enters an invalid menu option, display an error message, and display the menu again so the user can clearly see the valid menu options. Don’t display the menu after every input. Use a function to display the menu.
•	Use data validation to make sure the user can’t enter data that doesn’t make sense (such as a negative number of hits or the player having more hits than at bats).
•	Use try…except code to handle the exceptions that occur if the user enters a string where an integer is expected.
•	Make sure that no error occurs if the user enters zero for the number of at bats. This occurs before the first game of the season when all players have zero at bats. 

PART 2
•	Use the BaseballPlayers.csv file that is on the assignment page as the source for the lineup. The name of the file will be managed as a constant in the FileIO module.
•	Store the functions for writing to and reading from the file of players in a separate module named FileIO.py. Use the csv module for file I/O operations. 
•	The function that reads the file will return the list of players and have no parameters. 
•	The function that writes to the file will take a lineup list as the only input parameter and will not return anything. 
•	For part 2 replace the statement in the main method that declares the lineup list with a statement that calls the read method in the FileIO module. Call the write method of the FileIO module in any function that modifies the lineup list. Note: the line of code that declares a lineup list can be commented out for future debugging use.  
•	Handle the exception that occurs if the program can’t find the data file. The read function should return an empty list and the program should not end.

Use a top-down development process. For example, start by writing a main method that calls a  function that prints the title. Test the program and fix any errors. Then add a function that prints the menu options, call the function from the main method, test it, and move on to the next feature. 
Get as much of the Part 1 functions completed before moving on to Part 2. 
Make sure that there is always a working version that can be turned in even if it is incomplete. 
Projects will require the use of material from previous chapters covered in the textbook. 
Create a Team Management Python program that satisfies the specifications above. Turn in a single project, that is, only part 2 is needed.
Put General Comments at the beginning of the project that includes (1) your name, (2) the project name, (3) the date, and (4) a description of the project. 
Turn in a ZIP file of the final version of the program. Include a Word document which contains output of the testing done on the program. The Word document must be inside the ZIP file.
In the Comments section on the Assignment webpage, report (A) an estimate of the time it took to complete the project. Report a single value in minutes, and (B) a single rating of the project, on an ordinal scale, as either (1) Easy, (2) Moderate, (3) Hard, OR (4) Challenging. 
