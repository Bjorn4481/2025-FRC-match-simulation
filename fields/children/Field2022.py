from ..Field import Field
from scoring_locations.children.Hub2022 import Hub2022
from gamepieces.children.Cargo2022 import Cargo2022


class Field2022(Field):
    def __init__(self):
        super().__init__()
        self.scoring_locations = [Hub2022()]    
        self.add_cargo_to_field()

    def add_cargo_to_field(self):
        for i in range(11):
            self.gamepieces.append(Cargo2022("blue"))
            self.gamepieces.append(Cargo2022("red"))
        print("Added Cargo to field:")
        print(self.gamepieces)