from ..Robot import Robot
from scoring_locations.children.Hub2022 import Hub2022
from gamepieces.children.Cargo2022 import Cargo2022
import random

class Robot2022(Robot):
    def __init__(self):
        super().__init__()
        self.storage_capacity = 2
        self.storage = []
        self.climb_speed = 0.0
        self.climb_level = ["None", "Low", "Mid", "High", "Traversal"]
        self.intake_speed = 0.0
        self.shooter_speed = 0.0
        self.shooter_range = 0.0
        self.accuracy = 0.0

    def intake(self):
        if len(self.storage) < self.storage_capacity:
            self.storage.append(Cargo2022)
            print("ball added to storage")
        else:
            print("Storage is full!")

    def shoot_low(self):
        if len(self.storage) > 0:
            self.storage.pop()
            #Hub2022.score_low()
            print("ball removed from storage")

    def shoot_high(self):
        if len(self.storage) > 0:
            self.storage.pop()
            #Hub2022.score_high()
            print("ball removed from storage")
    
    def climb(self):
        climb_time = random.uniform(self.climb_speed - 2, self.climb_speed + 2)
        if self.climb_level == "None":
            pass
        else:
            print("Robot2022 climbed to level: ", self.climb_level, "within ", climb_time, " seconds")

    
        