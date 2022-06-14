#open input file
import os
here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'input.txt')
input = open(filename, "r")
afn = {}

#string cleanup
def strCleanup(str):
    str = str.replace("\n","")
    str = str.replace(" ","")
    return str.split(",")

#read input file
while (True):
    str = input.readline() #read line
    if "alfabeto=" in str: #save alphabet
        str = str.replace("alfabeto=","")
        afn["alfabeto"] = strCleanup(str)
        print(afn["alfabeto"])
    if "estados=" in str: #save states
        str = str.replace("estados=","")
        afn["estados"] = strCleanup(str)
        print(afn["estados"])
    if "inicial=" in str: #save initial state
        str = str.replace("inicial=","")
        afn["inicial"] = strCleanup(str)
        print(afn["inicial"])
    if "finais=" in str: #save final state
        str = str.replace("finais=","")
        afn["finais"] = strCleanup(str)
        print(afn["finais"])
    if "transicoes" in str: #save transitions
        afn["transicoes"] = {} #create dict entry for transitions
        afn["transicoes"]["epsilon"] = {} #create nested dict entry for empty transitions
        for i in afn["alfabeto"]: #create nested dict entry for each alphabet entry
            afn["transicoes"][i] = {}
        while (True): #read all the transition entries
            str = input.readline() #move to next transition
            if not str: #if no transitions left, stop
                break
            str = strCleanup(str) #get transition values
            if not str[0] in afn["transicoes"][str[2]]: #check if an entry already exists for jump-off state
                afn["transicoes"][str[2]][str[0]] = [] 
            if not str[1] in afn["transicoes"][str[2]][str[0]]: #check if duplicate transition
                afn["transicoes"][str[2]][str[0]].append(str[1])
        print(afn["transicoes"])            
    if not str:
        break
    
print(afn)

input.close()