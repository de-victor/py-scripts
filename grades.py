def generate_low_rank(list, indexes):
    return sorted([x[0] for index, x in enumerate(list) if index in indexes])

def generate_low_index(list):
    scores = [x[1] for x in list]
    return [index for index, value in enumerate(scores) if value == min(scores)]

def remove_lower(list, indexes):
    return [item for index, item in enumerate(list) if index not in indexes]

def find_low_ranks(list):
    low_index = generate_low_index(list)
    list = remove_lower(list, low_index)
    low_index = generate_low_index(list)

    return generate_low_rank(list, low_index)

if __name__ == '__main__':
    list = []
    for _ in range(int(input())):
        list.append([input(), float(input())])

    [print(x) for x in find_low_ranks(list)]