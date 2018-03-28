import re

def validation(p):
    size = len(p)
    index = 0
    jumps = 2
    cond = True
    while index < size and jumps < size and cond:
        cond = not (p[index] == p[jumps])
        index += 1
        jumps += 1


    return cond


if __name__ == "__main__":
    #"110000"
    p = "123456"

    print(validation(p))

    bo = not bool(re.search(r'[0-9]\d[0-9]', p))
    print(bo)

