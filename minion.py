from random import choice

def add_comb(comb, c):
    if c not in comb:
        comb.append(c)

def combinations(str, cons):
    comb = []
    c = ''
    i = 0
    while i < len(cons):
        indexes = sub_finds(str, cons[i])
        for j in indexes:
            for x in str[j:]:
                c += x
                if c in str:
                    add_comb(comb, c)
        i += 1
        c = ''

    return comb

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
    return indexes

def points(lis, str):
    points = 0
    for x in lis:
        points += len(sub_finds(str, x))
    return points

def vowel(str):
    vowels = ['A', 'E', 'I', 'O', 'U']
    return True if str in vowels else False

def seperat_vowels(str):
    return [x for x in str if vowel(x) and x.isalpha()]

def seperat_cons(str):
    return [x for x in str if not vowel(x) and x.isalpha()]

def minion_game(s):
    s = s.strip()
    kevin = combinations(s, seperat_vowels(s))
    stuart = combinations(s, seperat_cons(s))
    point_stu = points(stuart, s)
    point_ke = points(kevin, s)

    if point_stu > point_ke:
        print('Stuart {}'.format(point_stu))
    elif point_stu < point_ke:
        print('Kevin {}'.format(point_ke))
    else:
        print('Draw')

def gera_senha(tamanho):
    caracters = 'abcdefghijlmnopqrstuwvxz'
    senha = ''
    for char in range(tamanho):
        senha += choice(caracters)
    return senha.upper()

if __name__ == '__main__':
    #s = input().upper()
    s = gera_senha(5)
    print(s)
    kevin = combinations(s, seperat_vowels(s))
    stuart = combinations(s, seperat_cons(s))
    print(kevin)
    print(stuart)
    minion_game(s)
