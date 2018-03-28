def sub_finds(str = "", sub = ""):
    indexes = []
    i = str.find(sub)
    if i != -1:
        indexes.append(i)
        while True:
            i = str.find(sub, i+1)
            if i != -1:
                indexes.append(i)
            else:
                break
    return len(indexes)

def mutate_string(string, position, character):
    list = ['k' if index == position else c for index, c in enumerate(string)]
    return "".join(list)

def split_and_join(line):
    return "-".join(line.split(" "))

def up_low(str):
    list = [s.upper() if s.islower() else s.lower() for s in str]
    return "".join(list)

if __name__ == '__main__':
    str = 'ABCDCDCDC'

    print(sub_finds(str, 'C'))
