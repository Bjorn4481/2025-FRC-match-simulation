class Robot:
    def __init__(self):
        self.speed = 0.0
        self.acceleration = 0.0
        pass

    def __repr__(self):
        return self.__class__.__name__