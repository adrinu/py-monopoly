import pygame
import colors as Colors

class CheckBox:
    """Creates a CheckBox Object

        Args:
            screen (module): Configurations from user
            x (int): Distance from the left side of screen
            y (int): Distance from the top of screen
            width (int): Width of box  (Should be the same as Height)
            height (int): Height of box (Should be the same as Width)
            borderColor (module, optional): Color for the checkbox border. Defaults to Colors.black.
            checkColor (module, optional): Color for when the check box is checked. Defaults to Colors.black.
            uncheckedColor (module, optional): Color for when the checkbox is not checked. Defaults to Colors.boardColor.
            text (str, optional): Text to display next to checkbox. Defaults to "".
            textColor (module, optional): Color for text. Defaults to Colors.black.
            check (bool, optional): If the checkbox should be checked or not on creation. Defaults to False.
    """
    def __init__(self,screen, x, y, width, height, borderColor = Colors.black, checkColor = Colors.black, uncheckedColor = Colors.boardColor, text = "", textColor = Colors.black, check = False):
        
        self.screen = screen
        self.x = x
        self.y = y
        
        self.width = width
        self.height = height

        self.borderColor = borderColor
        self.checkColor = checkColor
        self.uncheckedColor = uncheckedColor
        
        self.text = text
        self.textColor = textColor

        self.check = check
    
    def draw(self):
        """Displays Checkbox on screen
        """

        # Create the border
        border = pygame.Rect(self.x , self.y, self.width, self.height)
        pygame.draw.rect(self.screen, self.borderColor, border )

        # Create the rectangle for inside
        inner = pygame.Rect(self.x + 10, self.y + 10, self.width - 20, self.height - 20)
        
        # If true, then the checkbox will be filled in
        if self.check:
            pygame.draw.rect(self.screen, self.checkColor, inner )
        # Checkbox is not filled in, so the inner square color should be the same color as the background
        else:
            pygame.draw.rect(self.screen, self.uncheckedColor, inner )

        # Create and Displays Text
        if self.text:
            font = pygame.font.SysFont(None, int(64 * (self.width / self.height)))
            img = font.render(self.text, True, self.textColor)

            self.screen.blit(img, (self.x + self.width + 10, self.y) )

    def isHover(self, pos):
        """Returns true if the mouse is hovering over the button

        Args:
            pos (tuple): Contains the x,y position of the mouse

        Return:
            bool: true or false
        """

        # Check if mouse is between the left and right side of the button
        if pos[0] > self.x and pos[0] < self.x + self.width:
            # Checks if mouse is between the top and bottom side of the button
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False