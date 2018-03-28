def create_tuple(max, maps):
    list = []
    count = 0
    for e in maps:
        list.append(e)
        count += 1
        if count == max:
            break
    return tuple(list)

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())

    t = create_tuple(n, integer_list)

    print(hash(t))