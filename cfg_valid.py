# LABORATORUL 4
# Apel in terminal cu: python cfgvalid.pyCFGuri/nume.txt , unde nume este numele fisierului CFG
import sys
import random


def load_cfg(filename):
    f = open(filename)
    g = f.readlines()
    g = [x.strip() for x in g]

    def getsectiune(keyword):
        auxx = []
        keyword += ':'
        poz = g.index(keyword)+1
        while g[poz] != 'End':
            auxx.append(g[poz])
            poz += 1
        return auxx

    l_var = getsectiune('Variables')
    l_term = getsectiune('Terminals')
    l_rel = getsectiune('Relations')

    for v in l_var:
        if v > 'Z' or v < 'A':
            print('Variabilele trebuie sa apartina intervalului A-Z!')
            exit()

    for t in l_term:
        if 'Z' > t > 'A':
            print('Terminalele nu pot apartine intervalului A-Z!')
            exit()

    for r in l_rel:
        aux = r.split(',')
        if aux[0] not in l_var:
            print(aux[0], " din Relations nu se gaseste in variables!")
            exit()
        for el in aux[1]:
            if el not in l_var and el not in l_term:
                print(el, " din Relations nu se gaseste nici in Variables, nici in Terminals!")
                exit()

    print(filename, " e valid!")
    return l_var, l_term, l_rel


var, term, rel = load_cfg(sys.argv[1])


def semirandom_cuv(rez):
    #   Semirandom ci nu random pentru ca regulile din CFG config sunt luate
    # in ordine, nu aleator. Fiecare regula este aplicata de un numar random
    # de ori (intre 0 si 10)
    global rel, term, var
    rel = [x.split(',') for x in rel]
    for r in rel:
        if rez == '':
            rez = r[0]
        cond = 0
        for lit in r[1]:
            if lit in var:
                cond = 1
        # daca nu sunt litere in sir inlocuim direct, pentru ca nu avem
        # din ce reguli sa substituim
        if cond:
            if len(r[1]) > 1:
                memo = r[0]
                for i in range(random.randint(0, 10)):
                    rez = rez.replace(memo, r[1])
            else: # acesta e cazul unei simple substitutii tip A <- B
                rez = rez.replace(r[0], r[1])
        else:
            rez = rez.replace(r[0], r[1])
    return rez


print(f"cuvant generat random in grammarul {sys.argv[1]}: ", repr(semirandom_cuv("").replace('#', '')))
# CARACTERUL # INSEAMNA LAMBDA / VID
