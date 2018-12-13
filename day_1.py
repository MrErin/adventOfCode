from my_data import frequency_changes


# part 1: get the frequency by adding each number together
print(sum(frequency_changes))


# part 2: find the first frequency that is duplicated when adding the numbers
each_frequency = []
frequency = 0
loop_counter = 0
stop = False

# this solution is comically inefficient. it took 137 seconds to complete.
# maybe next year I'll know how to do this better XD

for loop in range(0, 1000):
    if stop == False:
        for change in frequency_changes:
            frequency += change
            if frequency not in each_frequency:
                each_frequency.append(frequency)
            else:
                each_frequency.append(frequency)
                stop = True
                print(
                    f'The first duplicate is {frequency}. It was found during loop {loop_counter}.')
                break
    loop_counter += 1

print('done')
