# ---------------------------------------------------------------------------- #
#                                   Settings                                   #
# ---------------------------------------------------------------------------- #

# Sreen settings for the user
import pygame
# ---------------------------------------------------------------------------- #

# Dimensions for Application
WIDTH = 1600
HEIGHT = 900
size = (WIDTH, HEIGHT)

# If Application is in Fullscreen mode or not
isFullScreen = False

# Settings for the screen (e.g FullScreen, Resizeable window)
flagSettings = 0

# Screen to display to user
screen = pygame.display.set_mode(size, flags=flagSettings)

# Puts text on application window
pygame.display.set_caption("Monopoly Python")

# A list of availiable screen sizes
screenSizes = [(1920,1080), (1680,1050), (1600,900), (1440,900), (1280,720)]



