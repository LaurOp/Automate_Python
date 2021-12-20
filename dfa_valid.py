# LABORATORUL 1
# Apel in terminal cu: python dfa_valid.py DFAuri/nume.txt , unde nume este numele fisierului DFA

import sys


def computeDFA(filename):
    f = open(filename)
    g = f.readlines()
    f.close()
    g = [x.strip().lower() for x in g if x[0] != '#']

    def getsectiune(keyword):
        auxx = []
        keyword += ':'
        poz = g.index(keyword)+1
        while g[poz] != 'end':
            auxx.append(g[poz])
            poz += 1
        return auxx

    sigma = getsectiune('sigma')
    states = getsectiune('states')
    trans = getsectiune('transitions')
    statesl = [x.split(',')[0] for x in states]

    for el in trans:
        if len(el.split(',')) != 3:
            print("eroare de trans")
            exit()

    nrsuri = 0
    for el in states:
        aux = el.split(',')[1:]
        aux = [x.lower() for x in aux]
        if len(aux) > 2:
            print("eroare de states")
            exit()
        if len(aux) == 2:
            if aux[0] == aux[1]:
                print("eroare de states #2")
                exit()
        if 's' in aux:
            nrsuri += 1
        if nrsuri > 1:
            print("eroare S-uri")
            exit()

    if nrsuri == 0:
        print("nu avem start state")
        exit()

    for el in trans:
        aux = el.split(',')

        if aux[0] not in statesl or aux[2] not in statesl:
            print("eroare de states in trans")
            exit()
        if aux[1] not in sigma:
            print("eroare de sigma in trans")
            exit()

    print(sys.argv[1], " e valid!")
    return sigma, states, trans


computeDFA(sys.argv[1])
