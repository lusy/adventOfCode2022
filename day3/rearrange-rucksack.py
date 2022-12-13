def read_input():
    with open("input.txt") as input_file:
        return input_file.readlines()


def sum_wrong_items():
    all_backpacks = [line.rstrip() for line in read_input()]
    priorities_sum = 0

    for line in all_backpacks:
        halfmark = int(len(line) / 2)
        compart1 = line[:halfmark]
        compart2 = line[halfmark:]
        for item in compart1:
            if (item in compart2):
                priorities_sum += itemscore(item)
                break

    return priorities_sum


def sum_badges():
    all_backpacks = [line.rstrip() for line in read_input()]
    all_backpacks_groups_of_three = [all_backpacks[i:i+3] for i in range(0, len(all_backpacks), 3)]
    priorities_sum = 0

    for triple in all_backpacks_groups_of_three:
        for item in triple[0]:
            if (item in triple[1] and item in triple[2]):
                priorities_sum += itemscore(item)
                break

    return priorities_sum


def itemscore(item):
    if item.islower():
        return ord(item) - 96
    else:
        return ord(item) - 38


#print(sum_wrong_items())
print(sum_badges())

