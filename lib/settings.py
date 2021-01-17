import pygame
# ---------------------------------------------------------------------------- #
#                                   Settings                                   #
# ---------------------------------------------------------------------------- #

# Sreen settings for the user

# ---------------------------------------------------------------------------- #


# Displays the window 
WIDTH = 1600
HEIGHT = 1000
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size, pygame.RESIZABLE)

# Puts text on application window
pygame.display.set_caption("Monopoly Python")

# Returns a list of availiable screen sizes
screenSizes = pygame.display.list_modes()

def setScreenSize(index):
    """
    Sets the size of the window

    Args:
        index (int): Button index corresponding to the desired screen size
    """
    screen = pygame.display.set_mode(screenSizes[index], pygame.RESIZABLE)



