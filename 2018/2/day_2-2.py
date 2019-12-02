from day_2_data import box_labels

for label1 in box_labels:
    for label2 in box_labels:
        difference = 0
        for i in range(len(label1)):
            if label1[i] != label2[i]:
                difference += 1
        if difference == 1:
            winner = []
            for i in range(len(label1)):
                if label1[i] == label2[i]:
                    winner.append(label1[i])
            print(''.join(winner))
