** start of main.py **

import copy
import random

class Hat:
    def __init__(self,**kwargs):
        self.contents =[]
        for color,count in kwargs.items():
            self.contents.extend([color]*count)

    def draw(self,number_balls):
        if number_balls >= len(self.contents):
            draw = self.contents.copy()
            self.contents.clear()
            return draw
        else:
            draw = random.sample(self.contents, number_balls)
        for ball in draw:
            self.contents.remove(ball)
        return draw

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_count = 0
    for _ in range(num_experiments):
        trial_hat = copy.deepcopy(hat)
        drawn_balls = trial_hat.draw(num_balls_drawn)
        counts = {}
        for ball in drawn_balls:
            counts[ball] = counts.get(ball, 0) + 1
        success = True
        for color, count in expected_balls.items():
            if counts.get(color, 0) < count:
                success = False
                break
        if success:
            success_count += 1
    return success_count / num_experiments


** end of main.py **

