
# ---------------------------------------------------------------------------- #
#                                 TEXTBOX CLASS                                #
# ---------------------------------------------------------------------------- #
import pygame
import lib.colors as Colors
# ---------------------------------------------------------------------------- #

class TextBox:
    """Creates a TextBox object

        Args:
            screen (module): Screen to display the Textbox
            x (int): distance from left of screen
            y (int): distance from top of screen
            width (int): width of textbox
            height (int): height of textbox
            charLimit (int): Amount of characters allowed to be inputted
            borderColor (Colors, optional): Color for border . Defaults to Colors.black.
            backgroundColor (Colors, optional): background color for textbox. Defaults to Colors.boardColor.
            textColor (Colors, optional): Color for text inside the textbox. Defaults to Colors.white.
            selected (bool): If the user has clicked on the textbox or not
            selectedColor (Colors, optional): Border color if the textbox is selected. Defaults to Colors.black
        """
    def __init__(self, screen, x, y, width, height, charLimit, borderColor = Colors.black, backgroundColor = Colors.boardColor, textColor = Colors.white, textSize = 24, selected = False, selectedColor = Colors.white):
        
        self.screen = screen
        self.x = x
        self.y = y

        self.width = width
        self.height = height

        self.borderColor = borderColor
        self.backgroundColor = backgroundColor
        
        self.text = ""
        self.textSize = textSize
        self.textColor = textColor
        self.charLimit = charLimit

        self.selected = selected
        self.selectedColor = selectedColor
        
    
    def draw(self):
        """Draws the textbox onto screen
        """
         # Draws the box shape
        rectangle = pygame.Rect(self.x , self.y, self.width, self.height)

        # If selected, then we need to update the color to notify the user they are entering in that text box
        if self.selected:
            pygame.draw.rect(self.screen, self.selectedColor, rectangle)
        # User has deselected the textbox
        else:
            pygame.draw.rect(self.screen, self.borderColor, rectangle)

         # Create the rectangle for inside
        inner = pygame.Rect(self.x + 10, self.y + 10, self.width - 20, self.height - 20)
        pygame.draw.rect(self.screen, self.backgroundColor, inner )

        # Create Text
        font = pygame.font.SysFont(None, self.textSize)
        img = font.render(self.text, True, self.textColor)
        
        # Draws the text in the textbox
        self.screen.blit(img, (self.x + 20, self.y + self.height / 3) )


    def deleteChar(self):
        """Deletes a character from the textbox
        """
        if len(self.text) != 0:
            self.text = self.text[:-1]
    
    def addChar(self, char):
        """Adds a character to the textbox
        """
        if self.withinLimit():
            self.text += char

    def withinLimit(self):
        """Returns a bool if the user input text is over the character limit

        Returns:
            bool: true or false
        """
        return len(self.text) <= self.charLimit

    def isSelected(self, pos):
        self.selected = False
        # Check if mouse is between the left and right side of the button
        if pos[0] > self.x and pos[0] < self.x + self.width:
            # Checks if mouse is between the top and bottom side of the button
            if pos[1] > self.y and pos[1] < self.y + self.height:
                self.selected = True