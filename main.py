# Python implementation of a genetic solution to the Traveling Salesman Problem. This solution uses mutation to
# solicit small changes from the most successful entries in the pool. At every generation, the pool is replenished
# with random entrants to keep the genetic pool fresh and diverse. My experimentation showed that roughly 200
# generations was the upper limit of improvement, and 50 was sufficient in most cases.

# import packages/modules
import random
from random import randrange
import dist


# run the second gen onwards.
def second_gen_on():
    temp0 = genepoollist[0].copy()
    temp1 = genepoollist[1].copy()
    temp2 = genepoollist[2].copy()
    temp3 = genepoollist[3].copy()
    temp4 = genepoollist[4].copy()
    genepoollist[5] = mutator(temp0)
    genepoollist[6] = mutator(temp1)
    genepoollist[7] = mutator(temp2)
    genepoollist[8] = mutator(temp3)
    genepoollist[9] = mutator(temp4)
    for b in range(10, 20):
        random.shuffle(entrant20)
        genepoollist[b] = entrant20.copy()
    for a in range(len(genepoollist)):
        runner(genepoollist[a])

    print("Generation: ", counter)
    print(fitnessfunc(genepoollist[0]))


# check the value of the new entrant against the fittest members.
def runner(routelist):
    val = fitnessfunc(routelist)
    if val < fitnessfunc(genepoollist[0]):
        genepoollist[4] = genepoollist[3].copy()
        genepoollist[3] = genepoollist[2].copy()
        genepoollist[2] = genepoollist[1].copy()
        genepoollist[1] = genepoollist[0].copy()
        genepoollist[0] = routelist.copy()
    elif val < fitnessfunc(genepoollist[1]):
        genepoollist[4] = genepoollist[3].copy()
        genepoollist[3] = genepoollist[2].copy()
        genepoollist[2] = genepoollist[1].copy()
        genepoollist[1] = routelist.copy()
    elif val < fitnessfunc(genepoollist[2]):
        genepoollist[4] = genepoollist[3].copy()
        genepoollist[3] = genepoollist[2].copy()
        genepoollist[2] = routelist.copy()
    elif val < fitnessfunc(genepoollist[3]):
        genepoollist[4] = genepoollist[3].copy()
        genepoollist[3] = routelist.copy()
    elif val < fitnessfunc(genepoollist[4]):
        genepoollist[4] = routelist.copy()


# Get the total distance of the route given.
def fitnessfunc(routelist):
    fitnessvalue = 0
    for x in range(len(routelist) - 1):
        temp = routelist[x][routelist[x + 1]["name"]]
        fitnessvalue = fitnessvalue + temp

    temp2 = routelist[0][routelist[14]["name"]]
    fitnessvalue = fitnessvalue + temp2
    return fitnessvalue


# 50% chance to generate a mutated child of the top 5 fittest parents. 50% chance to produce a random entrant.
def mutator(routelist):
    temp0 = randrange(10) % 2
    if temp0 == 0:
        temp1 = randrange(15)
        temp2 = randrange(15)
        placeholder = routelist[temp1]
        routelist[temp1] = routelist[temp2]
        routelist[temp2] = placeholder
        return routelist
    else:
        temp3 = routelist.copy()
        random.shuffle(temp3)
        return temp3


# main function, includes the first generation and setup.
if __name__ == '__main__':
    citylist = [dist.atlanta, dist.boston, dist.chicago, dist.dallas, dist.denver, dist.houston, dist.lasvegas,
                dist.losangeles, dist.miami, dist.neworleans, dist.newyork, dist.phoenix, dist.sanfrancisco,
                dist.seattle, dist.washington]
    genepoollist = [citylist, citylist, citylist, citylist, citylist, citylist, citylist, citylist, citylist, citylist,
                    citylist, citylist, citylist, citylist, citylist, citylist, citylist, citylist, citylist, citylist]
    counter = 1

    entrant1, entrant2, entrant3, entrant4, entrant5, entrant6, entrant7, entrant8, entrant9, \
    entrant10 = citylist.copy(), citylist.copy(), citylist.copy(), citylist.copy(), citylist.copy(), citylist.copy(), citylist.copy(), citylist.copy(), citylist.copy(), citylist.copy()
    entrant11, entrant12, entrant13, entrant14, entrant15, entrant16, entrant17, entrant18, entrant19, \
    entrant20 = citylist.copy(), citylist.copy(), citylist.copy(), citylist.copy(), citylist.copy(), citylist.copy(), citylist.copy(), citylist.copy(), citylist.copy(), citylist.copy()
    random.shuffle(entrant1)
    random.shuffle(entrant2)
    random.shuffle(entrant3)
    random.shuffle(entrant4)
    random.shuffle(entrant5)
    random.shuffle(entrant6)
    random.shuffle(entrant7)
    random.shuffle(entrant8)
    random.shuffle(entrant9)
    random.shuffle(entrant10)
    random.shuffle(entrant11)
    random.shuffle(entrant12)
    random.shuffle(entrant13)
    random.shuffle(entrant14)
    random.shuffle(entrant15)
    random.shuffle(entrant16)
    random.shuffle(entrant17)
    random.shuffle(entrant18)
    random.shuffle(entrant19)
    random.shuffle(entrant20)
    runner(entrant1)
    runner(entrant2)
    runner(entrant3)
    runner(entrant4)
    runner(entrant5)
    runner(entrant6)
    runner(entrant7)
    runner(entrant8)
    runner(entrant9)
    runner(entrant10)
    runner(entrant11)
    runner(entrant12)
    runner(entrant13)
    runner(entrant14)
    runner(entrant15)
    runner(entrant16)
    runner(entrant17)
    runner(entrant18)
    runner(entrant19)
    runner(entrant20)
    for y in range(200):
        second_gen_on()
        counter += 1
    for r in range(15):
        temp = genepoollist[0]
        print(temp[r]["name"], "-> ", end='')
    print(temp[0]["name"])
