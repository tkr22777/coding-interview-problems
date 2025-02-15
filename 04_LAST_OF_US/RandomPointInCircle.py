from typing import List
import math, random


class Solution:
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self) -> List[float]:
        # sin y / d
        rand_r = random.random() * self.radius
        angle = random.random() * 360.0

        rand_y = rand_r * math.sin(math.pi / (angle * 180.0))
        rand_x = math.sqrt(rand_r * rand_r - rand_y * rand_y)

        # print(math.sin(0))
        # print(math.sin(90))
        # print(math.sin(180 * math.pi))

        return [self.x + rand_x, self.y + rand_y]

    # Your Solution object will be instantiated and called as such:


obj = Solution(5, 0, 0)
# param_1 = obj.randPoint()

print(obj.randPoint())