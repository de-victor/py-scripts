from random import randint

def constroi_tab(n,m):
    lista = []
    for i in range(n):
        lista.append(constroi_linha(m))
    return lista

def constroi_linha(m):
    lista = []
    for _, index in enumerate(range(m)):
        lista.append(gerar_bomba())
    return lista

def gerar_bomba():
    number = randint(0, 10000)
    return '*' if number %2 == 0 else '-'

def print_tab(tab):
    [print(x) for x in tab]

if __name__ == '__main__':
    tab = constroi_tab(*list(map(int, input('Informe o tamanho do tabuleiro(ex: 7 7): ').split(' '))))

    jogando = True
    pos = [-1, -1]

    while jogando and pos[0] != 'sair':
        print_tab(tab)
        pos = input('Informe pos ou digite sair ').split(' ')