def operations(i, op = []):
    if len(i) == 3:
        op.insert(i[1], i[2])
    if i[0] == 'print':
        print(op)
    if len(i) == 2 and i[0] == 'append':
        op.append(i[1])
    if len(i) == 2 and i[0] == 'remove':
        op.remove(i[1])
    if i[0] == 'sort':
        op.sort()
    if i[0] == 'pop':
        op.pop()
    if i[0] == 'reverse':
        op.reverse()

if __name__ == "__main__":
    n = int(input())

    commands = []
    op = []

    for i in range(n):
        list  = input().split(' ')
        commands.append(list)

    for i in commands:
        operations(i, op)