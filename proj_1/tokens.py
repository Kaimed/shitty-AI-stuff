#Python 3
#Simple Token Game AI PROJ 1 -- KEVIN CORPENY
#BY: KEVIN C CORPENY
################################################################################
from random import randint
from math import floor
################################################################################
#FUNCTIONALITY
def generate_losses(n):
    '''GENERATES ALL LOSING NUMBERS UP TO n AND RETURNS THEM IN A LIST'''
    lst = []
    add_factor = 2
    i = 1
    while(i <= n):
        lst.append(i)
        i = i+add_factor
        add_factor *= 2
    return lst
LOSER_LIST = generate_losses(500)

def chance_of_winning(n):
    '''returns the chance of winning With n tokens and how many tokens to take to achieve this chance.. This assumes both players will use my algorithm.'''
    losing_target = 1
    for x in range(0,8):
        if(LOSER_LIST[x] == n):
            #print("{} tokens to begin...You lose.".format(n))
            return 0
        elif(LOSER_LIST[x]>n):
            losing_target = LOSER_LIST[x-1]
            break
        elif(n>LOSER_LIST[7]):
            losing_target = LOSER_LIST[7]
            break
    correct_move = n-losing_target

    return correct_move

def game():
    win_list = []
    for n in range(1,501):
        if n in range(1,4):
            if(chance_of_winning(n) == 0):
                win_list.append("With {} tokens beginning, you lose... a 0{} chance of winning..\n".format(n,'%'))
            else:
                win_list.append(('With {} starting tokens, taking {} gives you a 100{} chance of winning!\n'.format(n,chance_of_winning(n),'%')))

        best_move = 1
        for k in range(1,floor(n/2)):
            if(chance_of_winning(n) != 0):
                best_move = chance_of_winning(n)
                win_list.append(('With {} starting tokens, taking {} gives you a 100{} chance of winning!\n'.format(n,best_move,'%')))
                break
            else:
                win_list.append("With {} tokens beginning, you lose... a 0{} chance of winning..\n".format(n,'%'))
                break
    return win_list

out = open('output.txt','w')
for tup in game():
    print(tup,file = out)
out.close()
