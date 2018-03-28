def is_alphanum(str = ''):
    cond = False
    for c in str:
        cond = c.isalnum()
        if cond:
            break
    print(cond)

def is_alphabe(str = ''):
    cond = False
    for c in str:
        cond = c.isalpha()
        if cond:
            break
    print(cond)

def is_digi(str = ''):
    cond = False
    for c in str:
        cond = c.isdigit()
        if cond:
            break
    print(cond)

def is_lower(str = ''):
    cond = False
    for c in str:
        cond = c.islower()
        if cond:
            break
    print(cond)

def is_upper(str = ''):
    cond = False
    for c in str:
        cond = c.isupper()
        if cond:
            break
    print(cond)

if __name__ == '__main__':
    str = 'qA2'

    is_alphanum(str)
    is_alphabe(str)
    is_digi(str)
    is_lower(str)
    is_upper(str)