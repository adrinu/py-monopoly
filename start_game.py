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
    
    players = [textbox.TextBox(Settings.screen, 500, 500, 500, 125, 8)]

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

        # Displays the play Button
        playButton = button.Button(Settings.screen, Settings.WIDTH - 10 - (Settings.WIDTH / 6), Settings.HEIGHT - (Settings.HEIGHT * .1), Settings.WIDTH / 6, Settings.HEIGHT / 12, "Play")
        playButton.draw()

        for tbb in players:
            tbb.draw()

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
                
                # Checks each textbox if it was selected or not
                for tb in players:
                    tb.isSelected(mousePosition)
            
            # 768 represents the user pressing BACKSPACE
            if event.type == 768:
                # For each textbox
                for tb in players:
                    # If it is selected
                    if tb.selected:
                        # Delete a character
                        if event.key == 8:
                            tb.deleteChar()
                        # Add a character
                        else:
                            tb.addChar(event.unicode)
        # --- Update the screen with what was drawn
        pygame.display.flip()
     
        # --- Limit to 60 frames per second
        clock.tick(60)
