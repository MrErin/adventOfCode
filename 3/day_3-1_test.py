import re
from collections import Counter

# should return both 1 and 2 because they are both in the same plots
# so the answer is 2
test_data = [
    {"claim_num": 1, "from_left": 1, "from_top": 3, "width": 4, "height": 4},
    {"claim_num": 2, "from_left": 3, "from_top": 1, "width": 4, "height": 4},
    {"claim_num": 3, "from_left": 5, "from_top": 5, "width": 2, "height": 2},
]

# the question is how many square inches of fabric are within two or more claims


def squares(c): return ((i, j) for i in range(c[1], c[1]+c[3])
                        for j in range(c[2], c[2]+c[4]))


fabric = Counter(s for c in test_data for s in squares(c))

part1 = sum(1 for v in fabric.values() if v > 1)
part2 = next(c[0] for c in test_data if all(
    fabric[s] == 1 for s in squares(c)))
