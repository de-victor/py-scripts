if __name__ == '__main__':
    x = 1
    y = 1
    z = 1
    n = 2
    #list = [x for x in range(9)]
    #list = [[x, y] for x in range(9) for y in range(9)]
    list = [[i,j,l] for i in range(0,x+1)
                    for j in range(0,y+1)
                    for l in range(0,z+1)
                    if i+j+l != n
            ]

    print(list)