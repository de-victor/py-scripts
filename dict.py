def mean(dictionary = {}, name = ""):
    selected = dictionary.get(name)
    sum = 0
    for x in selected:
        sum += x

    return "{:.2f}".format(round(float(sum/len(selected)),2))

if __name__ == '__main__':
    n = int(input())
    student_marks = {'mark': [10.0, 20.0, 30.0], 'jess': [30.0, 20.0, 50.0]}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    print(mean(student_marks, query_name))