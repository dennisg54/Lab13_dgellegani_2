import pygame.font
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Button:
    
    def __init__(self, game: 'AlienInvasion', msg) -> None:
        """
        Initialize the button's attributes.
        This method sets the button's position, size, color, and font.

        Args:
            game (AlienInvasion): The game instance.
            msg (str): The message to be displayed on the button.           
        """
        self.game = game
        self.screen = game.screen
        self.boundaries = game.screen.get_rect()
        self.settings = game.settings
        self.font = pygame.font.Font(
            self.settings.font_file, 
            self.settings.button_font_size
            )
        self.rect= pygame.Rect(0, 0, self.settings.button_w, self.settings.button_h)
        self.rect.center = self.boundaries.center
        self._prep_msg(msg)
       
    def _prep_msg(self, msg):
        """
        Turn the message into a rendered image and center it on the button.
        
        Args:
            msg (str): The message to be displayed on the button.
        """
        self.msg_image = self.font.render(msg, True, self.settings.text_color, None)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        
    
    def draw(self) -> None:
        """
        Draw the button on the screen.
        """
        self.screen.fill(self.settings.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
        
        
    def check_clicked(self, mouse_pos) -> bool:
        """
        Check if the button has been clicked.
        
        Args:
            mouse_pos (tuple): The position of the mouse cursor.
            
        Returns:
            bool: True if the button is clicked, False otherwise.
        """
        return self.rect.collidepoint(mouse_pos)