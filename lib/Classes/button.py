import pygame
import colors as Colors
class Button:
    def __init__(self, screen, x, y , width, height, text = "" , color = Colors.black, textColor = Colors.black):
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
        