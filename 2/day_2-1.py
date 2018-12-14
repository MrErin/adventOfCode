from collections import Counter
from day_2_data import box_labels

twos = 0
threes = 0

for box in box_labels:
    count = Counter(box)
    if len([k for k, v in count.items() if v == 2]) > 0:
        twos += 1
    if len([k for k, v in count.items() if v == 3]) > 0:
        threes += 1

print(f'checksum is {twos * threes}')
