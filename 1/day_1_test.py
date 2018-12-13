test_data = [1, -2, 3, 1]
frequency = 0
each_frequency = []
loop_counter = 0
stop = False

for loop in range(0, 100):
    if stop == False:
        for change in test_data:
            # print(f'the frequency is {frequency}')
            frequency += change
            # print(f'after adding {change}, the new frequency is {frequency}')
            if frequency not in each_frequency:
                each_frequency.append(frequency)
            else:
                each_frequency.append(frequency)
                stop = True
                print(
                    f'The first duplicate is {frequency}. It was found during loop {loop_counter}.')
                break
        loop_counter += 1


if __name__ == "__main__":
    print(f'the sum is {sum(test_data)}')
    print(f'full frequency list: {each_frequency}')
