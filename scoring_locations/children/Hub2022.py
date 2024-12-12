from ..ScoringLocation import ScoringLocation
from gamepieces.children.Cargo2022 import Cargo2022

class Hub2022(ScoringLocation):
    def __init__(self):
        super().__init__()

    def score_low(self):
        print("Low Hub scored!")

    def score_high(self):
        print("High Hub scored!")

    

