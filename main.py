import input
import simul

afn = input.getAFN("input.txt")
user_input = list("11010")

slist = simul.simulation(afn,user_input)
for entry in range(len(slist)):
    print(slist[entry])