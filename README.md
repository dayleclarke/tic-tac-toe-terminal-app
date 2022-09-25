# Animal Tic-Tac-Toe 
---
## [Github Repo](https://github.com/dayleclarke/tic-tac-toe-terminal-app)
## [Source Control Repo](https://github.com/dayleclarke/tic-tac-toe-terminal-app/commits/main)
## [Video Link](https://youtu.be/h-h2Lzclsws)
---

## Statement of Purpose and Scope

"Animal Tic-Tac-Toe” is a terminal(command line) application which is a variation on the classic Tic-Tac-Toe (or noughts and crosses) game.  In the game two players (one human user against one computer user) will take turns placing an X or O marker on a three-by-three grid.  The winner is whichever player is first to place three of their markers in a horizonal, vertical or diagonal row. If both players play optimally the game will end in a draw.

The purpose of this application is to demonstrate my ability to design, implement and test a terminal application and throughout the process demonstrate my ability to  use a range of developer tools. It was a mandatory requirement to accept user input and to either produce printed output or interact with a file system.

## Target Audience

The target market for this application is broad as it is a game that can be enjoyed by players of any age or gender. It is designed to be played by people who are somewhat tech savvy but haven't yet discovered the strategy to consistently win or tie the game.

---

## Features

* An Easy mode Person vs. Environment (PvE) 

The user can select to play on easy mode against a computer-controlled player.  The easy computer player will randomly select where to position their marker based on the free positions available on the board.  There are two easy computer players the user can select from: Pete the Panda or Katie the Koala.  

* An Expert mode Person vs. Environment (PvE) 

The user can select to play on expert mode against a computer-controlled player.  The expert computer player will select the optimal position to place their marker each time.  It is an unbeatable player which will either win or tie all games. When an expert play goes first it will position their marker in one of the corner positions. At all other times this player will invoke a recursive minimax function to return the optimal position based which position has the highest utility score (after testing all the possible free moves on the board).  There are two expert computer players the user can select from: Ollie the Octopus and Danni the Dolphin (both known to be highly intelligent animals).

* Game play order is determined by the outcome of a Scissor’s-Paper-Rock game

A game of scissors-paper-rock is played to determine which player will go first in the game.   Both players will simultaneously play either rock, paper, or scissors.  ASCII images of hands forming each of these gestures will be displayed. Rock (a closed fist) crushes scissors (two fingers forming a “V”), scissors cuts paper (a flat hand) and paper covers rock. In other words, rock wins against scissors, scissors win against paper and paper wins against rock.  The winner of scissors-paper-rock will be the first to place their marker. If both players make the same hand gesture than the game is repeated until a winner is determined. There is a distinct advantage to going first in Tic-Tac-Toe. 

## Reference List
David Middlehurst. (2022). ASCII.co. Retrieved September 20, 2022, from OCTOPUS - ASCII ART: https://ascii.co.uk/art/octopus
Karlsson, V. (2022). Hand Gestures- Nonverbal Communication - Signals. Retrieved September 19, 2022, from Injosoft ASCII Art Archive: https://www.asciiart.eu/people/body-parts/hand-gestures
Kwasniewski, M. '. (2022). Dolphins. Retrieved September 20, 2022, from Injosoft ASCII Art Archive: https://www.asciiart.eu/animals/dolphins
lgbeard. (2022). Fireworks. Retrieved September 20, 2022, from Injosoft ASCII Art Archive: https://www.asciiart.eu/holiday-and-events/fireworks
Stark, J. G. (2022). Marsupials. Retrieved September 20, 2022, from Injosoft ASCII Art Archive: https://www.asciiart.eu/animals/marsupials
Stark, J. G. (2022). Pandas. Retrieved September 20, 2022, from Injosoft ASCII Art Archive: https://www.asciiart.eu/animals/dolphins



For consistency and readability of code https://peps.python.org/pep-0008/

The criteria states: Uses input and output in TWO OR MORE SOPHISTICATED ways in an application, demonstrating DEEP AND NUANCED UNDERSTANDING of input and output in Python. I think I have multiple forms of output- (my program updates player's score in a separate csv file,  and there are lots of different types of print statements (ASCII font, tables as well as standard text) but the only input I take from the user is from input statements. If we get  (although these have yes/no responses, multiple choice questions, free form string statements such as entering their name) and that are converted into integers.  