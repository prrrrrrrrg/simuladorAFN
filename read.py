def strCleanup(str, type):
        str = str.replace("\n","")
        str = str.replace(" ","")
        if not str:
            return []
        if type == 2:
            return list(str)
        if type == 1:
            return str.split(",")
        if type == 0:
            return str
        
def getAFN(filename):
    #open input file
    import os
    here = os.path.dirname(os.path.abspath(__file__))
    input = open(os.path.join(here, filename), "r")
    afn = {}

    #read input file
    print("AFN Carregado:\n")
    while (True):
        str = input.readline() #read line
        if "%" in str:
            continue
        if "alfabeto=" in str: #save alphabet
            str = str.replace("alfabeto=","")
            afn["alfabeto"] = strCleanup(str,1)
            afn["alfabeto"].append("epsilon")
            print("ALFABETO ", afn["alfabeto"])
            continue
        if "estados=" in str: #save states
            str = str.replace("estados=","")
            afn["estados"] = strCleanup(str,1)
            print("ESTADOS ", afn["estados"])
            continue
        if "inicial=" in str: #save initial state
            str = str.replace("inicial=","")
            afn["inicial"] = strCleanup(str,1)
            print("ESTADO INICIAL ", afn["inicial"])
            continue
        if "finais=" in str: #save final state
            str = str.replace("finais=","")
            afn["finais"] = strCleanup(str,1)
            print("ESTADO FINAL ", afn["finais"])
            continue
            
        #error checkup
        if not "alfabeto" in afn: raise Exception("Alfabeto não encontrado.")
        if not "estados" in afn: raise Exception("Estados não encontrados.")
        for a in afn["alfabeto"]:
            if a in afn["estados"]: raise Exception("Alfabeto não pode possuir nomenclatura igual a estado.")
        if not "inicial" in afn: raise Exception("Estado inicial não encontrado.")
        if "" in afn["inicial"]: raise Exception("Estado inicial deve ser preenchido.")
        if not afn["inicial"][0] in afn["estados"]: raise Exception("Estado inicial não foi definido como estado.")
        if len(afn["inicial"]) == 2: raise Exception("Mais de um estado inicial foi definido.")
        if not "finais" in afn: raise Exception("Estados finais não encontrados.")
        
        if "transicoes" in str: #save transitions
            afn["transicoes"] = {} #create dict entry for transitions
            for i in afn["alfabeto"]: #create nested dict entry for each alphabet entry
                afn["transicoes"][i] = {}
            while (True): #read all the transition entries
                str = input.readline() #move to next transition
                if not str: #if no transitions left, stop
                    break
                str = strCleanup(str,1) #get transition values
                if not len(str) == 3:
                    raise Exception("Transições escritas incorretamente.")
                else:
                    if not str[0] in afn["estados"]: raise Exception("Estado em transição não foi definido.")
                    if not str[1] in afn["estados"]: raise Exception("Estado em transição não foi definido.")
                    if not str[2] in afn["alfabeto"]: raise Exception("Alfabeto em transição não foi definido.")
                
                if not str[0] in afn["transicoes"][str[2]]: #check if an entry already exists for jump-off state
                    afn["transicoes"][str[2]][str[0]] = [] 
                if not str[1] in afn["transicoes"][str[2]][str[0]]: #check if duplicate transition
                    afn["transicoes"][str[2]][str[0]].append(str[1])
            print("\nTRANSIÇÕES")
            for i in afn["alfabeto"]:
                for j in afn["transicoes"][i]:
                    print(j, "--", i, "->", afn["transicoes"][i][j])

        if not "alfabeto" in afn: raise Exception("Alfabeto não encontrado.")
        if not "estados" in afn: raise Exception("Estados não encontrados.")
        for a in afn["alfabeto"]:
            if a in afn["estados"]: raise Exception("Alfabeto não pode possuir nomenclatura igual a estado.")
        if not "inicial" in afn: raise Exception("Estado inicial não encontrado.")
        if "" in afn["inicial"]: raise Exception("Estado inicial deve ser preenchido.")
        if not afn["inicial"][0] in afn["estados"]: raise Exception("Estado inicial não foi definido como estado.")
        if len(afn["inicial"]) == 2: raise Exception("Mais de um estado inicial foi definido.")
        if not "finais" in afn: raise Exception("Estados finais não encontrados.")
        if not "transicoes" in afn: raise Exception("Transições não encontradas.")
        if not str:
            break
    
    input.close()
    return afn

