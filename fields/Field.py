class Field:
    def __init__(self):
        self.scoring_locations = []
    
    def start_match(self):
        for scoring_location in self.scoring_locations:
            scoring_location.start()
            print(f"Scoring location {scoring_location} started")

    def __repr__(self):
        return self.__class__.__name__
    