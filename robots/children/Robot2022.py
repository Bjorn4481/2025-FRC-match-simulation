from ..Robot import Robot

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
        #Check if there is enough space in the storage
        #If there is, add the gamepiece to the storage
        print("Robot2022.intake()")

    def shoot(self):
        #Check if there is a gamepiece in the storage
        #If there is, remove the gamepiece from the storage
        print("Robot2022.shoot()")
    
    def climb(self):
        #Check climb level
        #Check climb speed
        print("Robots2022.climb()")

    
        