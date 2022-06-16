import input
import simul

afn = input.getAFN("input.txt")
user_input = list("aaba")

slist = simul.simulation(afn,user_input)
for entry in range(len(slist)):
    print(slist[entry])