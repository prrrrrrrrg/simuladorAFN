def simulation(afn, user_input):
    slist = [[afn["inicial"][0]]]
    sclist = [slist[0][0]] #state cursor list
    
    def checkTransitions(afn,s_cursor,i_cursor):
        #if the current state has already crashed
        if s_cursor == "OUT_OF_BOUNDS":
            return -1
        #if the current state does not have a transition for the current input
        if not s_cursor in afn["transicoes"][user_input[i_cursor]]:
            return 0
        #if the current state does have a transition for the current input
        else:
            return range(len(afn["transicoes"][user_input[i_cursor]][s_cursor]))
        
    def branch(trans_range,afn,i_cursor,b_cursor):
        local_slist = slist[b_cursor].copy()
        local_sclist = sclist[b_cursor]
        
        if trans_range == -1:
            return 0
        
        if trans_range == 0:
            slist[b_cursor].append("CRASHED")
            sclist[b_cursor] = "OUT_OF_BOUNDS"
            return 0
                
        for no in trans_range:
            if not no == 0:
                slist.append(local_slist.copy())
                slist[-1].append(afn["transicoes"][user_input[i_cursor]][local_sclist][no])
                sclist.append(afn["transicoes"][user_input[i_cursor]][local_sclist][no])
            else:
                slist[b_cursor].append(afn["transicoes"][user_input[i_cursor]][local_sclist][no])
                sclist[b_cursor] = afn["transicoes"][user_input[i_cursor]][local_sclist][no]
        return 1
    
    for i in range(len(user_input)): #for every user input (i is index counter)
        for j in range(len(slist)): #for every branch
            branch(checkTransitions(afn,sclist[j],i),afn,i,j)
            
            if i + 1 == len(user_input):
                if sclist[j] in afn["finais"]:
                    slist[j].append("SUCCESS")
                else:
                    if not sclist[j] == "OUT_OF_BOUNDS":
                        slist[j].append("FAILURE")
            
    return slist