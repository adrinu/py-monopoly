# ---------------------------------------------------------------------------- #
#                               MAIN MENU SCREEN                               #
# ---------------------------------------------------------------------------- #
# When the user first runs the applications
# From here the user can set how many players, their names, change options
# and play of course!


# The insertion is needed to get the other dependecies to work
import pygame
import sys
sys.path.insert(1, "C:\\Users\\adria\\Desktop\\py-monopoly\\lib")
sys.path.insert(1, "C:\\Users\\adria\\Desktop\\py-monopoly\\lib\\Fonts")
sys.path.insert(1, "C:\\Users\\adria\\Desktop\\py-monopoly\\lib\\Classes")

import settings as Settings
import colors as Colors
import button

import options
# ---------------------------------------------------------------------------- #

pygame.init()
# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

def mainMenu(Settings):
    """Renders the main menu page

    Args:
        Settings (module): Configurations for the user
    """
    
    
    while True:
        # ---------------------------------------------------------------------------- #
        #                                 DRAWING CODE                                 #
        # ---------------------------------------------------------------------------- #

        # Sets screen color to sea foam green
        Settings.screen.fill(Colors.boardColor)

        # Creates the background behind the Monopoly Text
        rectangle = pygame.Rect(Settings.WIDTH / 8, Settings.HEIGHT / 12, ( Settings.WIDTH - (Settings.WIDTH * .25)), Settings.HEIGHT / 4)
        pygame.draw.rect(Settings.screen, Colors.red, rectangle)
        
        rectangle2 = pygame.Rect(Settings.WIDTH / 7, Settings.HEIGHT / 19, ( Settings.WIDTH - (Settings.WIDTH * .285)), Settings.HEIGHT / 3.25)
        pygame.draw.rect(Settings.screen, Colors.red, rectangle2)

        # Draws top left circle
        pygame.draw.circle(Settings.screen, Colors.red, (Settings.WIDTH / 6.925, Settings.HEIGHT/12), 31 )
        
        #Draws top right circle
        pygame.draw.circle(Settings.screen, Colors.red, ( ((Settings.WIDTH / 7) + Settings.WIDTH - (Settings.WIDTH * .286)), Settings.HEIGHT / 12), 30 )

        # Draws bottom left circle
        pygame.draw.circle(Settings.screen, Colors.red, (Settings.WIDTH / 6.925, Settings.HEIGHT/3.055), 31 )
        
        # Draws bottom right circle
        pygame.draw.circle(Settings.screen, Colors.red, (((Settings.WIDTH / 7) + Settings.WIDTH - (Settings.WIDTH * .286)), Settings.HEIGHT/3.055), 31)
        
        aspectRatio = Settings.WIDTH / Settings.HEIGHT

        # Displays the 'Monopoly' Text
        font = pygame.font.Font(None, int(72 * aspectRatio))
        txt = font.render("Monopoly", True, Colors.white)
        Settings.screen.blit(txt, (Settings.WIDTH / 2.5, Settings.HEIGHT / 6))

        # Displays the 'The Yonkers Edition' Text
        font = pygame.font.Font(None, int(27 * aspectRatio))
        txt = font.render("The Yonkers Edition", True, Colors.white)
        Settings.screen.blit(txt, (Settings.WIDTH / 2.35, Settings.HEIGHT / 3.75))
        
        # Displays an Option Button
        startButton = button.Button(Settings.screen, Settings.WIDTH / 2.35, Settings.HEIGHT / 2.25, Settings.WIDTH / 6, Settings.HEIGHT / 12, "Play")
        startButton.draw()

        # Displays an Option Button
        optionButton = button.Button(Settings.screen, Settings.WIDTH / 2.35, Settings.HEIGHT / 1.75, Settings.WIDTH / 6, Settings.HEIGHT / 12, "Option")
        optionButton.draw()

        # Displays the Quit Button
        quitButton = button.Button(Settings.screen, Settings.WIDTH / 2.35, Settings.HEIGHT / 1.45, Settings.WIDTH / 6, Settings.HEIGHT / 12, "Quit")
        quitButton.draw()

        # ---------------------------------------------------------------------------- #
        #                                  GAME LOGIC                                  #
        # ---------------------------------------------------------------------------- #

        for event in pygame.event.get():  # User did something
            mousePosition = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:  # If user clicked close
                pygame.quit() 

            # 1025 represents is user presses their Left Mouse Button
            if event.type == 1025:
                # Check if user is hovering over the play button
                if startButton.isHover(mousePosition):
                    # Checks if users presses their mouse button
                    if event.button == 1:
                        # Quits the game and program
                        print("Start button pressed")

                # Check if user is hovering over the option button
                if optionButton.isHover(mousePosition):
                    # Checks if users presses their mouse button
                    if event.button == 1:
                        # Navigatate to Options 
                        options.option(Settings)

                # Check if user is hovering over the quit button
                if quitButton.isHover(mousePosition):
                    # Checks if users presses their mouse button
                    if event.button == 1:
                        # Quits the game and program
                        pygame.quit()
                        sys.exit()

        # --- Update the screen with what was drawn
        pygame.display.flip()
     
        # --- Limit to 60 frames per second
        clock.tick(60)


if __name__ == "__main__":
    mainMenu(Settings)