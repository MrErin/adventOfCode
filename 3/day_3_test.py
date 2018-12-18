import re
from collections import Counter
import os

# should return both 1 and 2 because they are both in the same plots
# so the answer is 4 (a 2x2 area is covered by multiple rectangles)

# the question is how many square inches of fabric are within two or more claims

# this stuff just sets up and opens the raw data file
here = os.path.dirname(os.path.realpath(__file__))
test_data = 'day_3_testdata.txt'
test_data_filepath = os.path.join(here, test_data)
input = open(test_data_filepath, "r")

# this line reads the raw data and breaks it into a list of lists of only the numeric values in each line
# especially interesting is the regex (r'\d+'). That filters out everything that isn't a number or a set of numbers
claims = [[*map(int, re.findall(r'\d+', l))] for l in input if l]

print(claims)


def squares(c): return ((x_axis, y_axis)
                        # these lines map out the coordinates of the rectangles.
                        # x_axis takes the start position number (which is the second number in each list) and extends it by the width of the x_axis (coordinates: start = start, end = start + width)
                        for x_axis in range(c[1], c[1]+c[3])
                        # same calculation taking place for the y_axis, except for length rather than width
                        for y_axis in range(c[2], c[2]+c[4]))


# this line says the entire piece of fabric is a Counter that will tally the number of overlap inches.
# the list comprehension reads "for every list (claim), create a square in the fabric"
# the counter creates a dictionary of sets that describe every inch of the fabric and counts the number of rectangles occupying that inch.
fabric = Counter(s for c in claims for s in squares(c))
print(fabric)

# This line creates a ticker that increments for each inch in the fabric that is occupied by two or more squares, which is the solution to part 1 of the puzzle.
part1 = sum(1 for v in fabric.values() if v > 1)

# this part outputs the id (c[0]) of a claim that is not overlapped by any other rectangles
# next returns the next item in an iterator
# the comprehension reads "if every inch described by this claim == 1, print the claim number"
part2 = next(c[0] for c in claims if all(
    fabric[s] == 1 for s in squares(c)))

print(part1)
print(part2)
