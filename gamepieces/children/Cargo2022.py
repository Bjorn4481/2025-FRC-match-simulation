from ..Gamepiece import Gamepiece
import time

class Cargo2022(Gamepiece):
    def __init__(self, color):
        super().__init__()
        self.color = color

    def bounce(self):
        print("bouncing")
        time.sleep(3)

    