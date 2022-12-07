"""File that deals with scoring in the game"""
import time

class Score:
    """Class to keep track of the score"""
    def __init__(self):
        self.start_time = 0
        self.end_time = 0
        self.finished = False

    def start_timer(self):
        """starts the timer"""
        self.start_time = time.time()

    def stop_timer(self):
        """stops the timer"""
        self.end_time = time.time()
        self.finished = True

    def get_score(self):
        """returns current score as seconds elapsed"""
        if self.finished:
            return self.end_time - self.start_time
        if self.start_time == 0:
            return 0
        return int(time.time() - self.start_time)
