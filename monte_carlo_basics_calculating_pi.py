#Monte Carlo
# Calculating Pi

# Area of a circle is pi * r * r
# Area of the squared around the circle is 4 * r * r
# Ratio of the area of circle to the square pi * r * r / 4 * r * r --> pi / 4
# To find Pi, find the ratio of the area of the circle to the square * 4

import random

def generate_random_point() -> (float, float):
    x = random.uniform(0, 1)    # unifor is very important, eucledian dispersion or other will not work
    y = random.uniform(0, 1)
    return x, y

def is_point_in_circle(point : (float, float)) -> bool:
    if point[0]**2 + point[1]**2 <= 1:
        return True
    return False

num_in_circle = 0
num_in_square = 10000

for _ in range(num_in_square):
    point = generate_random_point()
    if is_point_in_circle(point):
        num_in_circle += 1

print("Pi statement after", num_in_square, "tiems", 4*num_in_circle/num_in_square)