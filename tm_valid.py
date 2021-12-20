# LABORATORUL 5
#    Apel in terminal cu: python tm_valid.py TMuri/nume.txt inp , unde nume este
# numele fisierlui TM iar inp este input stringul pe care il verificam
import sys


def load_tm(filename):
    f = open(filename)
    g = f.readlines()
    g = [x.strip() for x in g if len(x) and x[0] != '#']

    def getsectiune(keyword):
        auxx = []
        keyword += ':'
        poz = g.index(keyword) + 1
        while g[poz] != 'End':
            auxx.append(g[poz])
            poz += 1
        return auxx

    states = getsectiune('States')
    inpalfabet = getsectiune('Input alphabet')
    tape = getsectiune('Tape alphabet')
    trans = getsectiune('Transitions')
    start, accept, reject = '', '', ''
    for el in g:
        if 'Start state: ' in el:
            start = el.split(': ')[1]
    for el in g:
        if 'Accept state: ' in el:
            accept = el.split(': ')[1]
    for el in g:
        if 'Reject state: ' in el:
            reject = el.split(': ')[1]

    transaux = [x.split(' ') for x in trans]

    if start not in states:
        print('Eroare start in states')
        exit()
    if accept not in states:
        print('Eroare accept in states')
        exit()
    if reject not in states:
        print('Eroare reject in states')
        exit()

    for tr in transaux:
        if tr[0] not in states or tr[1] not in states:
            print('Eroare in trans, nu exista state-ul!')
            exit()
        if tr[2] not in tape:
            print('Eroare in trans, nu exista tape input-ul!')
            exit()
        if tr[3] not in tape and tr[3] != 'e':
            print('Eroare in trans pozitia 4')
            exit()
        if tr[4] not in 'LR':
            print('Eroare in trans pozitia 5')
            exit()

    print(f'{filename} este valid!')
    return states, inpalfabet, tape, transaux, start, accept, reject


def verif(filename, inp):
    states, inpalfabet, tape, trans, start, accept, reject = load_tm(filename)
    print(inp, ' este ', end='', sep='')
    inp = list(inp + '_')
    poz = 0

    # parcurgere inspirata din functia step() din sursa https://www.python-course.eu/turing_machine.php
    while start not in (accept, reject):
        # start il vom updata conform tranzitiilor
        # parcurgerea inputului pana ajungem pe o stare accept sau reject
        for tr in trans:
            if start == tr[0]:
                if inp[poz] == tr[2]:
                    start = tr[1]
                    if tr[3] != 'e':
                        inp[poz] = tr[3]
                    if tr[4] == 'R' and poz < len(inp):
                        poz += 1
                    else:
                        if poz - 1 >= 0:
                            poz -= 1
    if start == accept:
        print('ACCEPTAT')
    else:
        print('REFUZAT')

load_tm(sys.argv[1])
#verif(sys.argv[1], sys.argv[2])
