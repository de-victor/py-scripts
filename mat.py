def pipe(n):
    list = ['.|.' if type(x) == int else '.|.' for x in range(n)]
    return ''.join(list)

if __name__ == '__main__':
    n, m = list(map(int, input().split(' ')))

    qtd = 1
    mid = int(n / 2)

    for j in range(n):
        if j < mid:
            print(pipe(qtd).center(m, '-'))
            qtd += 2
        elif j > mid:
            qtd -= 2
            print(pipe(qtd).center(m, '-'))
        elif j == mid:
            print('WELCOME'.center(m, '-'))