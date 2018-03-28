def print_rangoli(size):
    print_mat(generate_mat(size))

def generate_mat(n):
    alphabet = [chr(i) for i in range(97, 97 + n)]
    wid = (len(alphabet) * 4) - 3
    let_count = len(alphabet) - 1
    ori = len(alphabet) - 1
    rag = []
    for _ in range(n):
        if let_count >= 0:
            tmp = 1 + ori - let_count
            str_r = ''
            str_l = ''
            if tmp != 0:
                ls = [value for index, value in enumerate(alphabet) if index in range(let_count + 1, let_count + tmp)]
                str_r = '-'.join(ls)
                ls.reverse()
                str_l = '-'.join(ls)
            if '-' in str_r or len(str_l) == 1:
                line = '{}-{}-{}'.format(str_l, alphabet[let_count], str_r).center(wid, '-')
                rag.append(line)
            else:
                line = '{}'.format(alphabet[let_count]).center(wid, '-')
                rag.append(line)
            let_count -= 1
    return rag

def print_mat(ran):
    [print(x) for x in ran]
    ran.reverse()
    [print(x) for index, x in enumerate(ran) if index != 0]

if __name__ == "__main__":
    n = int(input())

    print_rangoli(n)