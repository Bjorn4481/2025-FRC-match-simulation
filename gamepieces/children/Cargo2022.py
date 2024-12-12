from ..Gamepiece import Gamepiece
import time
from random import randint
from time import sleep

class Cargo2022(Gamepiece):
    def __init__(self, color):
        super().__init__()
        self.color = color

    def bounce(self):
        print("bouncing")
        time.sleep(3)

    def HubDelay(self):
        print("Delayed in hub")
        sleep(randint(1, 3))
        print("Scored in hub")

    