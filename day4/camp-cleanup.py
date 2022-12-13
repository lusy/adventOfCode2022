def read_input():
    with open("input.txt") as input_file:
        return input_file.readlines()


def compute_overlapping_areas():
    areas = read_input()
    counter = 0
    for line in areas:
        left, right = line.rstrip().split(',')
        left_begin, left_end = left.split('-')
        right_begin, right_end = right.split('-')
        #print(f'for the pair {left_begin}-{left_end} and {right_begin}-{right_end}')
        does_left_contain_right = int(left_begin) <= int(right_begin) and \
            int(left_end) >= int(right_end)
        does_right_contain_left = int(right_begin) <= int(left_begin) and \
            int(right_end) >= int(left_end)
        #print(f'does_left_contain_right = {does_left_contain_right}')
        #print(f'does_right_contain_left = {does_right_contain_left}')
        if does_left_contain_right  or does_right_contain_left:
            #print('incrementing counter')
            counter += 1

    return counter


def compute_intersecting_areas():
    areas = read_input()
    counter = 0
    for line in areas:
        left, right = line.rstrip().split(',')
        left_begin, left_end = left.split('-')
        right_begin, right_end = right.split('-')
        #print(f'for the pair {left_begin}-{left_end} and {right_begin}-{right_end}')
        dont_overlap = int(left_end) < int(right_begin) or int(right_end) < int(left_begin)
        #print(f'does_left_contain_right = {does_left_contain_right}')
        #print(f'does_right_contain_left = {does_right_contain_left}')
        if not dont_overlap:
            #print('incrementing counter')
            counter += 1

    return counter


#print(compute_overlapping_areas())
print(compute_intersecting_areas())
