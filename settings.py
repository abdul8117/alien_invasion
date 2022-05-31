class Settings:
    """A class to store all settings for the Alien Invasion game."""

    def __init__(self):
        """Initialise the game's settings."""

        # Screen settings
        self.screen_width = 0
        self.screen_height = 0
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 0.5