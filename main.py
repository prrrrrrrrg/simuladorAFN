import input
import simul

afn = input.getAFN("input.txt")
user_input = list("11010")
sdict = {}

simul.simulation(sdict,afn,user_input,afn["inicial"][0],0,0)