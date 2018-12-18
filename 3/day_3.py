import re
from collections import Counter
import os

# the question is how many square inches of fabric are within two or more claims

# this stuff just sets up and opens the raw data file
here = os.path.dirname(os.path.realpath(__file__))
data = 'day_3_data.txt'
data_filepath = os.path.join(here, data)
input = open(data_filepath, "r")

claims = [[*map(int, re.findall(r'\d+', l))] for l in input if l]


def squares(c): return ((x_axis, y_axis)
                        for x_axis in range(c[1], c[1]+c[3])
                        for y_axis in range(c[2], c[2]+c[4]))


fabric = Counter(s for c in claims for s in squares(c))

part1 = sum(1 for v in fabric.values() if v > 1)
part2 = next(c[0] for c in claims if all(
    fabric[s] == 1 for s in squares(c)))

print(part1)
print(part2)
