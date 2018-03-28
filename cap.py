def capitalize2(s = ''):
    ls = s.split(' ')
    ls2 = []
    str = ''
    for x in ls:
        str = x[0].upper()
        index = 1
        while index < len(x):
            str += x[index]
            index += 1
        ls2.append(str)
    return ' '.join(ls2)

def capitalize(s):
    ls = s.strip().split(' ')
    ls2 = [x[0].upper()+x[1:] if x.strip() != '' else x for x in ls]
    return ' '.join(ls2).strip()

if __name__ == '__main__':
    str = input()

    print(capitalize(str))

    str = 'teste teste'
    print(str.capitalize())

