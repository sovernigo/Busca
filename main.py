def gerarEstados(st): # l/s - quarto está limpo ou sujo // p/n presença ou não do aspirador

    listaDeEstados = list()

    # mover da sala esquerda suja
    estado = [0, st[1]]
    listaDeEstados.append(estado)

    # mover da sala direita suja
    estado = [st[0], 0]
    listaDeEstados.append(estado)

    # limpar sala esquerda
    estado = [2, st[1]]
    listaDeEstados.append(estado)

    # limpar sala direita
    estado = [st[0], 2]
    listaDeEstados.append(estado)

    # mover da sala esquerda limpa
    estado = [1, st[1]]
    listaDeEstados.append(estado)

    # mover da sala direita limpa
    estado = [st[0], 1]
    listaDeEstados.append(estado)

    if st[0] is 2:
        estado = [1, st[1]]
    else:
        estado = [0, st[1]]
    listaDeEstados.append(estado)

    if st[1] is 2:
        estado = [st[0], 1]
    else:
        estado = [st[0], 0]
    listaDeEstados.append(estado)

    return listaDeEstados


def isClean(st):

    if (st[0] == 1 and st[1] == 2) or (st[0] == 2 and st[1] == 1):
        return True
    else:
        return False


def son2str(st):
    return ''.join([str(v) for v in st])

def buscaEmLargura(start):
    cand = [start]
    pais = dict()
    visitado = [start]

    while(len(cand) > 0):
        noPai = cand[0]
        print('candidatos: ', cand)
        del cand[0]
        print('visitado: ', visitado)

        if(isClean(noPai)):
            res = []
            node = noPai
            while node is not start:
                res.append(node)
                node = pais[son2str(node)]
            res.append(start)
            res.reverse()
            print('Solução Encontrada: ', res)
            input()

        for filho in gerarEstados(noPai):
            if filho not in visitado:
                print('Inserido: ', filho, noPai)
                visitado.append(filho)
                pais[son2str(filho)] = noPai
                cand.append(filho)

buscaEmLargura([0,0])