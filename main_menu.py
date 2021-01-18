import pygame
import sys
sys.path.insert(1, "C:\\Users\\adria\\Desktop\\py-monopoly\\lib")
sys.path.insert(1, "C:\\Users\\adria\\Desktop\\py-monopoly\\lib\\Fonts")
sys.path.insert(1, "C:\\Users\\adria\\Desktop\\py-monopoly\\lib\\Classes")


import colors as Colors
import button
 
pygame.init()
# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

def mainMenu(Settings):
    """Renders the main menu page

    Args:
        Settings (module): Configurations for the user
    """
    
    height = Settings.HEIGHT
    width = Settings.WIDTH
    
    while True:
        # ---------------------------------------------------------------------------- #
        #                                 DRAWING CODE                                 #
        # ---------------------------------------------------------------------------- #

        # Sets screen color to sea foam green
        Settings.screen.fill(Colors.boardColor)

        # Creates the background behind the Monopoly Text
        rectangle = pygame.Rect(width / 8, height / 12, ( width - (width * .25)), height / 4)
        pygame.draw.rect(Settings.screen, Colors.red, rectangle)
        
        rectangle2 = pygame.Rect(width / 7, height / 19, ( width - (width * .285)), height / 3.25)
        pygame.draw.rect(Settings.screen, Colors.red, rectangle2)

        # Draws top left circle
        pygame.draw.circle(Settings.screen, Colors.red, (width / 6.925, height/12), 31 )
        
        #Draws top right circle
        pygame.draw.circle(Settings.screen, Colors.red, ( ((width / 7) + width - (width * .286)), height / 12), 30 )

        # Draws bottom left circle
        pygame.draw.circle(Settings.screen, Colors.red, (width / 6.925, height/3.055), 31 )
        
        # Draws bottom right circle
        pygame.draw.circle(Settings.screen, Colors.red, (((width / 7) + width - (width * .286)), height/3.055), 31)
        
        aspectRatio = width / height

        # Displays the 'Monopoly' Text
        font = pygame.font.Font(None, int(72 * aspectRatio))
        txt = font.render("Monopoly", True, Colors.white)
        Settings.screen.blit(txt, (width / 2.5, height / 6))

        # Displays the 'The Yonkers Edition' Text
        font = pygame.font.Font(None, int(27 * aspectRatio))
        txt = font.render("The Yonkers Edition", True, Colors.white)
        Settings.screen.blit(txt, (width / 2.35, height / 3.75))
        
        # Displays an Option Button
        optionButton = button.Button(Settings.screen, width / 2.35, height / 2, width / 6, height / 12, "Option")
        optionButton.draw()

        # Displays the Quit Button
        quitButton = button.Button(Settings.screen, width / 2.35, height / 1.65, width / 6, height / 12, "Quit")
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
                # Check if user is hovering over the option button
                if optionButton.isHover(mousePosition):
                    # Checks if users presses their mouse button
                    if event.button == 1:
                        # Navigatate to Options 
                        option(Settings)
                # Check if user is hovering over the quit button
                if quitButton.isHover(mousePosition):
                    # Checks if users presses their mouse button
                    if event.button == 1:
                        # Quits the game and program
                        pygame.quit()
                        sys.exit()

        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
     
        # --- Limit to 60 frames per second
        clock.tick(60)

def option(Settings):
    """
    docstring
    """
   pass


