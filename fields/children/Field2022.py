from ..Field import Field
from scoring_locations.children.Hub2022 import Hub2022

class Field2022(Field):
    def __init__(self):
        super().__init__()
        self.scoring_locations = [Hub2022()]
    
    