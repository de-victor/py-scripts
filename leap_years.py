def div_str(year, div):
    return "{}".format(round(year/div, 1))


def leap(year):
    leap = False
    if div_str(year, 4).endswith("0"):
        leap = True
        if div_str(year, 100).endswith("0"):
                leap = False
                if div_str(year, 400).endswith("0"):
                    leap = True

    return leap

if __name__ == "__main__":
    year = int(input("type year: "))

    print(leap(year))

