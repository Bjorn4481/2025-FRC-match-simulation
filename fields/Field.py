import simpy

class Field:
    def __init__(self):
        self.scoring_locations = []
        self.robots = []
        self.match_status = "waiting"
        self.match_time = 150.0 # seconds
        self.env = simpy.Environment()
    
    def start_match(self):
        for scoring_location in self.scoring_locations:
            scoring_location.start()
            print(f"Scoring location {scoring_location} started")
        for robot in self.robots:
            robot.start()
            print(f"Robot {robot} started")
        self.env.process(self.clock())
        self.env.run(until=self.match_time)
        
    def clock(self):
        while True:
            self.set_match_status()
            yield self.env.timeout(0.1)

    def set_match_status(self):
        if self.env.now >= self.match_time:
            self.match_status = "finished"
        elif self.env.now > 15:
            self.match_status = "teleop"
        elif self.env.now > 0:
            self.match_status = "auto"
        else:
            self.match_status = "waiting"

    

    def __repr__(self):
        return self.__class__.__name__
    