import copy
import random


class Hat:
    def __init__(self, **kwargs):
        self.contents = [k for k, v in kwargs.items() for i in range(v)]

    def draw(self, amount):
        draw_contents = []
        if amount < len(self.contents):
            for i in range(amount):
                draw_contents.append(self.contents.pop(random.randrange(len(self.contents))))
            return draw_contents
        else:
            for i in range(len(self.contents)):
                draw_contents.append(self.contents.pop())
            return draw_contents


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    right = 0
    exp = num_experiments
    while exp != 0:
        item_copy = copy.deepcopy(hat)
        drawn = item_copy.draw(num_balls_drawn)
        drawn_dict = {}
        check_dict = {}
        for i in drawn:
            drawn_dict[i] = drawn_dict.get(i, 0) + 1
        for k in drawn_dict.keys():
            if k in expected_balls.keys():
                check_dict[k] = check_dict.get(k, drawn_dict[k])
        if len(check_dict) == len(expected_balls):
            a = 0
            for k, v in check_dict.items():
                if expected_balls[k] == v or v > expected_balls[k]:
                    a += 1
            if a == len(expected_balls):
                right += 1
        exp -= 1
    prob = right / num_experiments
    return prob
