# part 2
# Find the two box ids that differ by exactly one character
# return only the letters these boxes have in common
# For the test data, the correct answer is "fghij" and "fguij", and should return "fgij"

test_data = ['abcde',
             'fghij',
             'klmno',
             'pqrst',
             'fguij',
             'axcye',
             'wvxyz']

# initialize the first side of the comparison ("x")
for x in test_data:
    # initialize the second side of the comparison ("y")
    for y in test_data:
        # initialize a counter for whether or not we have a match
        difference = 0
        # for each position in the length of string "x"...
        for i in range(len(x)):
            # if that character is different from the character in the same position in string "y"...
            if x[i] != y[i]:
                # add one to the difference counter
                difference += 1
        # at the end of it all, if the difference is exactly 1...
        if difference == 1:
            answer = []
            # push each of the matching characters to a list, "answer"
            for i in range(len(x)):
                if x[i] == y[i]:
                    answer.append(x[i])
            # join the "answer" list
            print(''.join(answer))
