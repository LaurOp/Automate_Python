# LABORATORUL 3
#   Apel in terminal cu: python nfa_2_dfa.py NFAuri/nume1.txt DFAuri/nume2.txt , unde nume1 este numele
# fisierului NFA iar nume2 este numele fisierului destinatie , in care vrem sa avem continutul noului
# DFA

import sys
import dfa_valid


def convertNFA_to_DFA(filenameNFA, filenameDFA):

    sigma, states, trans = dfa_valid.computeDFA(filenameNFA)

    trans2 = [(x.split(',')[0], x.split(',')[1], x.split(',')[2]) for x in trans]

    finale = []
    for x in states:
        if 'f' in x.split(','):
            finale.append(x.split(',')[0])
    finalei = finale

    startstate = ''
    for x in states:
        if 's' in x.split(','):
            startstate = x.split(',')[0]

    states = [x.split(',')[0] for x in states]

    i = 0

    trans3 = []
    # crearea de noi stari respectiv tranzitii:
    while i < len(states):
        for si in sigma:
            aux = []
            for el in states[i]:
                for tr in trans2:
                    if tr[0][0] == el and tr[1] == si:
                        if tr[2][0] not in aux:
                            aux.append(tr[2])

            if len(aux) > 1:
                if aux not in states:
                    states.append(aux)
                    for z in aux:
                        if z in finalei:
                            finale.append(aux)
                            break
            if len(aux):
                if len(aux) == 1:
                    trans3.append((states[i], si, aux[0]))
                else:
                    trans3.append((states[i], si, aux))
        i += 1

    a = ord('a')
    output = open(filenameDFA, 'w')
    # scrierea noului fisier-config DFA:
    output.write('Sigma:\n')
    for el in sigma:
        output.write("\t")
        output.write(el)
        output.write('\n')
    output.write('End\n')

    output.write('States:\n')
    for el in states:
        output.write("\t")
        output.write(chr(a))
        a += 1
        if len(el) == 1:
            if el == startstate:
                output.write(',s')
        if el in finale:
            output.write(',f')
        output.write('\n')
    output.write('End\n')

    a = ord('a')

    output.write('Transitions:\n')
    for el in trans3:
        output.write("\t")
        output.write(chr(states.index(el[0])+a))
        output.write(',')
        output.write(el[1])
        output.write(',')
        output.write(chr(states.index(el[2]) + a))
        output.write('\n')
    output.write('End\n')

    print('Fisierul ', filenameDFA, ' a fost creat')


convertNFA_to_DFA(sys.argv[1], sys.argv[2])
