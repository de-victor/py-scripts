if __name__ == '__main__':
    list = [2,3,6,6,5]
    top = max(list)
    top2 = max([x for x in list if x != max(list)])
    print(top2)