crates_map = {
    '1': ['F', 'R', 'W'],
    '2': ['P', 'W', 'V', 'D', 'C', 'M', 'H', 'T'],
    '3': ['L', 'N', 'Z', 'M', 'P'],
    '4': ['R', 'H', 'C', 'J'],
    '5': ['B', 'T', 'Q', 'H', 'G', 'P', 'C'],
    '6': ['Z', 'F', 'L', 'W', 'C', 'G'],
    '7': ['C', 'G', 'J', 'Z', 'Q', 'L', 'V', 'W'],
    '8': ['C', 'V', 'T', 'W', 'F', 'R', 'N', 'P'],
    '9': ['V', 'S', 'R', 'G', 'H', 'W', 'J']
}

test_crates_map = {
    '1': ['N', 'Z'],
    '2': ['D', 'C', 'M'],
    '3': ['P']
}


def read_input(source):
    with open(source) as input_file:
        return input_file.readlines()


def rearrange_crates(input_map, source_file):
    plan = read_input(source_file)
    for line in plan:
        _, count, _, origin, _, destination = line.rstrip().split(' ')
        list_to_move = input_map[origin][:int(count)]
        del input_map[origin][:int(count)]
        # comment in for part 1
        # list_to_move.reverse()
        input_map[destination][:0] = list_to_move

    result = []
    for stack in input_map:
        result.append(input_map[stack][0])
    print(''.join(result))


rearrange_crates(crates_map, 'input.txt')
