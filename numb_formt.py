def line(i, wid):
    return '{}'.format(i).rjust(wid,' ')

if __name__ == '__main__':
    i = 2
    wid = len(bin(i).replace('0b', ''))
    for n in range(1,i+1):
        print(line(n, wid), end='')
        print(line(oct(n).replace('0o',''), wid+1), end='')
        print(line(hex(n).upper().replace('0X',''), wid+1), end='')
        print(line(bin(n).replace('0b', ''), wid+1))

    print('1  1  1  1')
    print('2  2  2 10')

