
from pathlib import Path

class Settings:   
    def __init__ (self) -> None:
        """
        Initialize the game settings.
        This method sets the default values for various game parameters such as screen size,
        ship speed, bullet speed, alien speed, and sound file paths.
        It also sets the initial values for the ship and alien fleet.
        """
        # Initialize the game screen size settings and animation frame rate
        self.name: str = "Alien Invasion"
        self.screen_w: int = 1200
        self.screen_h: int = 800
        self.FPS = 60
        self.difficulty_scale = 1.1
        
        # Initialize the game background
        """
        self.bg_file source:
        Source URL: https://www.pexels.com/photo/space-background-11657224/
        filename: pexels-photo-11657224.jpeg
        """
        self.bg_file = Path.cwd() / "Assets" / "images" / "pexels-photo-11657224.png"
        
        # Initialize the game ship settings - the player's ship
        """
        self.ship_file source:
        Source URL: https://www.hiclipart.com/free-transparent-background-png-clipart-okdip
        original filename: starship-enterprise-harley-benton-television-fan-art-star-trek.jpg
        """
        self.ship_file = Path.cwd() / "Assets" / "images" / "starship(nobg).png"
        self.ship_w = 40
        self.ship_h = 60
        
        # Initialize the game bullet settings - the player's ship bullets
        self.bullet_file = Path.cwd() / "Assets" / "images" / "beam_nobg.png"
        
        # Initialize the game alien settings - the enemy ship
        """
        self.alien_file source:
        Source URL: https://www.pinterest.com/pin/klingon-bird-of-prey-token-by-thebalzan--527343437621168351/
        original filename: klingon-bird-of-prey-token-by-thebalzan.jpg
        """

        self.alien_file = Path.cwd() / "Assets" / "images" / "enemy_ship_nobg.png"
        self.alien_w = 40
        self.alien_h = 40
        self.fleet_direction = 1
        
        # Initialize the game sound settings
        """
        self.laser_sound source:
        Source URL: https://pixabay.com/sound-effects/search/laser/
        filename: laser-zap-90575.mp3
        
        self.impact_sound source:
        Source URL: https://pixabay.com/sound-effects/search/explosion/
        filename: explosion-312361.mp3
        """
        self.laser_sound = Path.cwd() / "Assets" / "sound" / "laser-zap-90575.mp3" # Ship firing sound                
        self.impact_sound = Path.cwd() / "Assets" / "sound" / "explosion-312361.mp3" # Impact sound for bullets hitting aliens        
        
        """
        Source URL: https://fonts.google.com/selection?categoryFilters=Appearance:%2FTheme%2FTechno
        filename: Audiowide
        """
        # Initialize the game button settings
        self.button_w = 200
        self.button_h = 50
        self.button_color = (116, 152, 242)
        self.text_color = (255, 255, 255)
        self.button_font_size = 48
        self.HUD_font_size = 25
        self.font_file = Path.cwd() / "Assets" / "Fonts" / "Audiowide" / "Audiowide-Regular.ttf"
        self.button_font_bold = True
        
        
    def initialize_dynamic_settings(self) -> None:
        """
        Initialize settings that change throughout the game.
        This method sets the initial values for the ship, bullet, and alien speeds.
        """
        self.ship_speed = 5
        self.starting_ship_amount = 3
        
        self.bullet_speed = 7
        self.bullets_amount = 5
        self.bullet_w = 25
        self.bullet_h = 80
        
        self.fleet_speed = 1
        self.fleet_drop_speed = 40
        
    def increase_difficulty(self) -> None:
        """
        Increase the game difficulty settings.
        This method increases the speed of the ship, bullet, and alien fleet.
        """
        self.ship_speed *= self.difficulty_scale
        self.bullet_speed *= self.difficulty_scale
        self.fleet_speed *= self.difficulty_scale