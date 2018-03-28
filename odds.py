def even(n):
    return n % 2 is 0


def odd_or_not(n):
    if not even(n):
        print("Weird")
    elif even(n) and n >= 2 and n <= 5:
        print("Not Weird")
    elif even(n) and n >= 6 and n <= 20:
        print("Weird 3")
    elif even(n) and n > 20:
        print("Not Weird")

if __name__ == '__main__':
    n = int(input("Type a number: "))
    odd_or_not(n)



