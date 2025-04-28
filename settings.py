
from pathlib import Path

class Settings:   
    def __init__ (self) -> None:
      
        self.name: str = "Alien Invasion"
        self.screen_w: int = 1200
        self.screen_h: int = 800
        self.FPS = 60
        self.bg_file = Path.cwd() / "Assets" / "images" / "pexels-photo-11657224.png"
        
        self.ship_file = Path.cwd() / "Assets" / "images" / "starship(nobg).png"
        self.ship_w = 40
        self.ship_h = 60
        self.ship_speed = 5
        self.starting_ship_amount = 3
        
        self.bullet_file = Path.cwd() / "Assets" / "images" / "beam_nobg.png"
        self.bullet_speed = 7
        self.bullet_w = 25
        self.bullet_h = 80
        self.bullets_amount = 5
        
        self.alien_file = Path.cwd() / "Assets" / "images" / "enemy_ship_nobg.png"
        self.alien_w = 40
        self.alien_h = 40
        self.fleet_speed = 2
        self.fleet_direction = 1
        self.fleet_drop_speed = 40
        
        self.laser_sound = Path.cwd() / "Assets" / "sound" / "sci-fi-weapon-laser-shot-04-316416.mp3"
        self.impact_sound = Path.cwd() / "Assets" / "sound" / "explosion-312361.mp3"
        
        
        