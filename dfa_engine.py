# LABORATORUL 2
#   Apel in terminal cu: python dfa_engine.py DFAuri/nume.txt inp , unde nume este numele fisierului
# DFA iar inp este input stringul despre care vrem sa stim daca este acceptat de automat
#   MENTIUNE: pentru rularea fisierelor dfa1.txt si dfa2.txt trebuie decomentata cealalta varianta
# de apel a functiei
import dfa_valid
import sys


def verif(inp_string):
    sigma, states, trans = dfa_valid.computeDFA(sys.argv[1])

    def getstarestart():
        for x in states:
            if 's' in x.split(','):
                return x.split(',')[0]

    def getstarifinale():
        finale = []
        for x in states:
            if 'f' in x.split(','):
                finale.append(x.split(',')[0])
        return finale

    def getdirdin(a):
        direct = []
        for x in trans:
            if x.split(',')[0] == a:
                direct.append(x)
        return direct

    def check(inp):
        vec = [x for x in inp]
        stare_curenta = getstarestart()
        fin = getstarifinale()
        for elem in vec:
            directii = [x.split(',') for x in getdirdin(stare_curenta)]
            cond = 0
            for elem2 in directii:
                if elem2[1] == elem:
                    cond = 1
                    stare_curenta = elem2[2]
                    break
            if cond == 0:
                print("Respins!")
                exit()

        if stare_curenta in fin:
            print("Acceptat!")
            exit()
        else:
            print("Respins!")

    check(inp_string)


verif(sys.argv[2])
# verif(sys.argv[2].split(',')) pentru dfa1 si dfa2
