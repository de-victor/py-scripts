def scale(n):
    index = 0
    while index < n:
        print(index * index)
        index += 1


if __name__ == "__main__":
    n = int(input("type number "))

    scale(n)
