# ---------------------------------------------------------------------------- #
#                                 OPTION SCREEN                                #
# ---------------------------------------------------------------------------- #
# This file creates the screen the user sees when they click on the options page
# in the main menu

# The insertion is needed to get the other dependecies to work
import pygame

import lib.colors as Colors
import lib.settings as Settings
import lib.Classes.button as button
import lib.Classes.checkbox as checkbox
# ---------------------------------------------------------------------------- #

pygame.init()
# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()


def option(Settings):
    """Creates the option page where users can select what resolution and if they want to play in fullscreen

    Args:
        Settings (module): Configurations for the user
    """
    # Bool to start/stop the loop
    running = True

    # Pre-generate the buttons for resolutions
    resolutions = generateResolutionButtons(Settings)

    while running:
        # ---------------------------------------------------------------------------- #
        #                                 DRAWING CODE                                 #
        # ---------------------------------------------------------------------------- #

        # Sets screen color to sea foam green
        Settings.screen.fill(Colors.boardColor)
       
        # Displays the Quit Button
        quitButton = button.Button(Settings.screen, 10, Settings.HEIGHT - (Settings.HEIGHT * .1), Settings.WIDTH / 6, Settings.HEIGHT / 12, "Go Back")
        quitButton.draw()

        # Displays Resolution Buttons
        for i in range(len(Settings.screenSizes)):
            resolutions[i].draw()

        # Creates and Displays Fullscreen Button
        fullscreen = checkbox.CheckBox(Settings.screen, 10, resolutions[-1].y + 110, 50, 50, check=Settings.isFullScreen, text="Fullscreen")
        fullscreen.draw()


        # ---------------------------------------------------------------------------- #
        #                                  GAME LOGIC                                  #
        # ---------------------------------------------------------------------------- #

        for event in pygame.event.get():  # User did something
            mousePosition = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:  # If user clicked close
                pygame.quit() 

            # 1025 represents is user presses their Left Mouse Button
            if event.type == 1025: 
                # Check if user is hovering over the quit button
                if quitButton.isHover(mousePosition):
                    # Checks if users presses their mouse button
                    if event.button == 1:
                        # Quits from the Option page and returns user to main menu
                        running = False
                
                # Checks if user is hovering over the fullscreen button
                if fullscreen.isHover(mousePosition):
                    # Checks if user presser their mouse button
                    if event.button == 1:
                        # Quits fullscreen
                        if Settings.isFullScreen:
                            newScreen = pygame.display.set_mode((Settings.WIDTH, Settings.HEIGHT))
                            Settings.screen = newScreen
                            Settings.isFullScreen = False
                        # Enter fullscreen
                        else:
                            newScreen = pygame.display.set_mode((Settings.WIDTH, Settings.HEIGHT), pygame.FULLSCREEN)
                            Settings.screen = newScreen
                            Settings.isFullScreen = True

                # Check every button and see if user is hovering to whichever button
                for i in range(len(resolutions)):
                    if resolutions[i].isHover(mousePosition):
                        if event.button == 1:
                            setScreenSize(i)
                            break

         # --- Update the screen with what was drawn
        pygame.display.flip()
     
        # --- Limit to 60 frames per second
        clock.tick(60)
            
def setScreenSize(index):
    """
    Sets the size of the window

    Args:
        index (int): Button index corresponding to the desired screen size
    """
    Settings.HEIGHT = Settings.screenSizes[index][1]
    Settings.WIDTH = Settings.screenSizes[index][0]
    newScreen = pygame.display.set_mode((Settings.WIDTH, Settings.HEIGHT), Settings.screen.get_flags())
    Settings.screen = newScreen

def generateResolutionButtons(Settings):
    """Generates a list containing buttons related to resolution size

    Args:
        Settings (module): Configuration for the user

    Returns:
        List: Contains the Button class
    """

    # Create a list of buttons with resolution sizes
    resolutionButtons = []
    
    positionX = 10
    positionY = 10

    for i in range(len(Settings.screenSizes)):
        resolutionString = str(Settings.screenSizes[i][0]) + " x " + str(Settings.screenSizes[i][1])

        temp = button.Button(Settings.screen, 0, 0, Settings.WIDTH - (Settings.WIDTH * .9), Settings.HEIGHT - (Settings.HEIGHT * .9), resolutionString, Colors.black)
        temp.x = positionX
        temp.y = positionY
        resolutionButtons.append(temp)
        positionY += 110
    
    return resolutionButtons
