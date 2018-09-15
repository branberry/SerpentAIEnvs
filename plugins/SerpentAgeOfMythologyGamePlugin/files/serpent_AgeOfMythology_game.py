from serpent.game import Game

from .api.api import AgeOfMythologyAPI

from serpent.utilities import Singleton




class SerpentAgeOfMythologyGame(Game, metaclass=Singleton):

    def __init__(self, **kwargs):
        kwargs["platform"] = "steam"

        kwargs["window_name"] = "Age Of Mythology"

        kwargs["app_id"] = "266840"
        kwargs["app_args"] = None
        
        
        

        super().__init__(**kwargs)

        self.api_class = AgeOfMythologyAPI
        self.api_instance = None

    @property
    def screen_regions(self):
        regions = {
            "SAMPLE_REGION": (0, 0, 0, 0)
        }

        return regions

    @property
    def ocr_presets(self):
        presets = {
            "SAMPLE_PRESET": {
                "extract": {
                    "gradient_size": 1,
                    "closing_size": 1
                },
                "perform": {
                    "scale": 10,
                    "order": 1,
                    "horizontal_closing": 1,
                    "vertical_closing": 1
                }
            }
        }

        return presets
