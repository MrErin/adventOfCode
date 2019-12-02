from collections import Counter

# part 1
# Should produce:
# count2: 4 total
# count3: 3 total
# checkSum should be 12 (4*3)

test_data = [
    'abcdef',
    'bababc',
    'abbcde',
    'abcccd',
    'aabcdd',
    'abcdee',
    'ababab'
]

two = 0
three = 0

for box in test_data:
    # Counter keeps track of how many times it encounters equivalent items
    count = Counter(box)
    if len([k for k, v in count.items() if v == 2]) > 0:
        two += 1
    if len([k for k, v in count.items() if v == 3]) > 0:
        three += 1

print(f'checksum is {two * three}')
