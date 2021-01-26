# ---------------------------------------------------------------------------- #
#                                 BUTTON CLASS                                 #
# ---------------------------------------------------------------------------- #
import pygame
import lib.colors as Colors
# ---------------------------------------------------------------------------- #

class Button:
    """Creates a button

        Args:
            screen ([type]): The screen for the button to be displayed to
            x (float): x coordinate
            y (float): y coordinate
            width (float): witdth
            height (float): height 
            color (Color): Color for the button
            text (str, optional): Text to display on the button. Defaults to "".
            textColor (Color): Color for the text
    """
    def __init__(self, screen, x, y , width, height, text = "" , color = Colors.black, textColor = Colors.black):
        self.screen = screen
        self.x = x
        self.y = y 
        self.width = width
        self.height = height
        self.text = text
        self.color = color
        self.textColor = textColor
        
    def draw(self):
        """Displays the button on the screen
        """
        # Draws the button shape
        rectangle = pygame.Rect(self.x , self.y, self.width, self.height)
        pygame.draw.rect(self.screen, self.color, rectangle)

        # If the button has text, then draw it 
        if self.text:
            # Create Text
            font = pygame.font.SysFont(None, int(24 * (self.width / self.height)))
            img = font.render(self.text, True, Colors.white)
            
            # Grabs height and width of Text
            textDimensions = img.get_rect()
            textWidth = textDimensions.width
            textHeight = textDimensions.height

            # Centers text within the button
            self.screen.blit(img, (self.x + (self.width / 2 - textWidth / 2), self.y + (self.height / 2 - textHeight / 2)))

    def isHover(self, pos):
        """Returns true if the mouse is hovering over the button

        Args:
            pos (tuple): Contains the x,y position of the mouse
        """

        # Check if mouse is between the left and right side of the button
        if pos[0] > self.x and pos[0] < self.x + self.width:
            # Checks if mouse is between the top and bottom side of the button
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False
        