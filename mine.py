from random import randint

def constroi_tab(n,m):
    lista = []
    for i in range(n):
        lista.append(constroi_linha(m))
    return lista

def gerar_field(field, index):
    bomba = gerar_bomba()
    field['lista'].append(bomba)
    field['indexes'].append(index) if bomba == '*' else ''
    field['qtd_bomba'] += 1 if bomba == '*' else 0

    return field
def constroi_linha(m):
    field = {'lista': [],
             'indexes': [],
             'qtd_bomba': 0}

    for _, index in enumerate(range(m)):
        gerar_field(field, index)

    return field

def gerar_bomba():
    number = randint(0, 10000)
    return '*' if number %2 == 0 else '-'

def print_tab(tab, jogadas):
    cont = 0
    explodiu = False
    while cont < len(tab) and not explodiu:

        for index, x in enumerate(tab[cont]['lista']):
            pos = [cont, index]
            if pos in jogadas:
                if x == '*':
                    explodiu = True
                    break
                else:
                    print('[ - ]'.format(cont, index), end='')
            else:
                print('[{}-{}]'.format(cont, index), end='')

        if explodiu:
            print('Explodiu, fim de jogo')
            break
        else:
            print()
        cont += 1

    return explodiu

if __name__ == '__main__':
    tab = constroi_tab(*list(map(int, input('Informe o tamanho do tabuleiro(ex: 7 7): ').split(' '))))
    jogadas = []
    jogando = True
    pos = [-1, -1]
    print_tab(tab, jogadas)

    while jogando and pos[0] != 'sair':
        pos = input('Informe pos ou digite sair ').strip().split(' ')

        if len(pos) == 2:
            pos = list(map(int, pos))
            if pos in jogadas:
                print('voce ja fez essa jogada!!!')
            else:
                jogadas.append(pos)
                jogando = not print_tab(tab, jogadas)