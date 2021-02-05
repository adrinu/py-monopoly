# ---------------------------------------------------------------------------- #
#                                  START GAME                                  #
# ---------------------------------------------------------------------------- #
# Users can set how many other local players want to play, must have atleast one other

import pygame

import lib.colors as Colors
import lib.settings as Settings
import lib.Classes.button as button
import lib.Classes.textbox as textbox

# ---------------------------------------------------------------------------- #

pygame.init()
# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()


def startGame(Settings):
    # Initializes the game with one player to start
    players = [(button.Button(Settings.screen, 0, Settings.HEIGHT / 12, 0, 0),textbox.TextBox(Settings.screen, Settings.WIDTH / 3, Settings.HEIGHT / 12, 500, 125, 8))]
    numPlayers = len(players)


    running = True
    while running:
        # ---------------------------------------------------------------------------- #
        #                                 DRAWING CODE                                 #
        # ---------------------------------------------------------------------------- #

        # Sets screen color to sea foam green
        Settings.screen.fill(Colors.boardColor)

        # Displays the back Button
        backButton = button.Button(Settings.screen, 10, Settings.HEIGHT - (Settings.HEIGHT * .1), Settings.WIDTH / 6, Settings.HEIGHT / 12, "Back")
        backButton.draw()

        # Creatges the add player Button
        addPlayerButton = button.Button(Settings.screen, Settings.WIDTH / 2.75, Settings.HEIGHT - (Settings.HEIGHT * .1), Settings.WIDTH / 4, Settings.HEIGHT / 12, "Add Player")
        
        # The game only supports 4 players
        if len(players) != 4: 
            addPlayerButton.draw()

        # Creates the play Button
        playButton = button.Button(Settings.screen, Settings.WIDTH - 10 - (Settings.WIDTH / 6), Settings.HEIGHT - (Settings.HEIGHT * .1), Settings.WIDTH / 6, Settings.HEIGHT / 12, "Play")
        
        # The game must have atleast 2 players inorder to play
        if 1 < len(players) <= 4:
            # Players must have a name
            if validateTextBoxes(players):
                # Displays the play button
                playButton.draw()

        # Display the remove player button and the textbox
        for i in range(len(players)):
            players[i][0].draw()
            players[i][1].draw()

        # ---------------------------------------------------------------------------- #
        #                                  GAME LOGIC                                  #
        # ---------------------------------------------------------------------------- #

        for event in pygame.event.get():  # User did something
            mousePosition = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:  # If user clicked close
                pygame.quit()

            # 1025 represents is user presses their Left Mouse Button
            if event.type == 1025:
                # Checks if the mouse was hovering over the back button when the LMB was clicked
                if backButton.isHover(mousePosition):
                    # Returns user to main menu
                    running = False

                # Checks if mouse is hovering over add player button
                if addPlayerButton.isHover(mousePosition):
                    # Check if the number of players is less than the max
                    if numPlayers < 4:
                        numPlayers += 1
                        players.append((button.Button(Settings.screen, Settings.WIDTH / 4, players[-1][0].y + 150, 125, 125, "X", 64), textbox.TextBox(Settings.screen, Settings.WIDTH / 3, players[-1][1].y + 150, 500, 125, 8)))
                
                if playButton.isHover(mousePosition):
                    pass

                # Checks each textbox if it was selected or not
                for tb in players:
                    tb[1].isSelected(mousePosition)

                # Checks each remove player button if it was clicked
                for j in range(len(players)):
                    # If player clicked on it
                    if players[j][0].isHover(mousePosition):
                        # Removes the player
                        removePlayer(players, j)
                        numPlayers -= 1
                        break


            # 768 represents the user pressing BACKSPACE
            if event.type == 768:
                # For each textbox
                for tb in range(len(players)):
                    # If it is selected
                    if players[tb][1].selected:
                        # Delete a character
                        if event.key == 8:
                            players[tb][1].deleteChar()
                        # Add a character
                        else:
                            players[tb][1].addChar(event.unicode)

        # --- Update the screen with what was drawn
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(60)


def removePlayer(lst, index):
    """Removes player from the game

    Args:
        lst (list): List contaning tuples of classes  -> (Button, TextBox)
        index (int): Index of player to be removed
    """

    for i in range(index, len(lst) - 1):
        # We swap the to-be-removed player's name towards the end of the list 
        # This allows the order of players to be the same while saving some operations :)
        lst[i][1].text, lst[i+1][1].text = lst[i+1][1].text, lst[i][1].text
    lst.pop()

def validateTextBoxes(lst):
    """Returns a bool if the list of text boxes all have text

    Args:
        lst (list): List contaning tuples of classes  -> (Button, TextBox)
    """

    for pair in lst:
        # If textbox does not have text
        if not pair[1].text:
            return False
    # has text
    return True