def simulation(afn, user_input):
    slist = [[afn["inicial"][0]]]
    sclist = [slist[0][0]] #state cursor list
    
    initial_pass_list = []
    for start in sclist:
        if start in afn["transicoes"]["epsilon"]:
            for new in range(len(afn["transicoes"]["epsilon"][start])):
                if afn["transicoes"]["epsilon"][start][new] in initial_pass_list:
                    continue
                slist.append([afn["transicoes"]["epsilon"][start][new]])
                sclist.append(afn["transicoes"]["epsilon"][start][new])
                initial_pass_list.append(afn["transicoes"]["epsilon"][start][new])
    
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
        #save the current state of the list before messing with it
        local_slist = slist[b_cursor].copy()
        local_sclist = sclist[b_cursor]
        #if crashed, do nothing
        if trans_range == -1:
            return 0
        #if there are no possible transitions, crash
        if trans_range == 0:
            slist[b_cursor].append("CRASHED")
            sclist[b_cursor] = "OUT_OF_BOUNDS"
            return 0
        #if there are possible transitions       
        for no in trans_range:
            #for all transitions except the first one, create a new branch
            if not no == 0:
                slist.append(local_slist.copy())
                b_cursor = len(slist) - 1
                slist[b_cursor].append(afn["transicoes"][user_input[i_cursor]][local_sclist][no])
                sclist.append(afn["transicoes"][user_input[i_cursor]][local_sclist][no])
            #for the first transition, stay in the same branch
            else:
                slist[b_cursor].append(afn["transicoes"][user_input[i_cursor]][local_sclist][no])
                sclist[b_cursor] = afn["transicoes"][user_input[i_cursor]][local_sclist][no]
            #for epsilon transitions in the destination state, create new branches
            def checkEpsilon(local_slist,sclist,b_cursor,afn,pass_list):
                if sclist[b_cursor] in afn["transicoes"]["epsilon"]:
                    for tr in range(len(afn["transicoes"]["epsilon"][sclist[b_cursor]])):
                        if afn["transicoes"]["epsilon"][sclist[b_cursor]][tr] in pass_list:
                            continue
                        slist.append(local_slist.copy())
                        ep_cursor = len(slist) - 1
                        slist[ep_cursor].append(afn["transicoes"]["epsilon"][sclist[b_cursor]][tr])
                        sclist.append(afn["transicoes"]["epsilon"][sclist[b_cursor]][tr])
                        pass_list.append(afn["transicoes"]["epsilon"][sclist[b_cursor]][tr])
                        checkEpsilon(local_slist,sclist,ep_cursor,afn,pass_list)        
            pass_list = []
            checkEpsilon(local_slist,sclist,b_cursor,afn,pass_list)
                    
        return 1
    
    for i in range(len(user_input)): #for every user input (i is index counter)
        for j in range(len(slist)): #for every branch
            branch(checkTransitions(afn,sclist[j],i),afn,i,j)
                        
    for l in range(len(slist)):
        if sclist[l] in afn["finais"]:
            slist[l].append("SUCCESS")
        else:
            if not sclist[l] == "OUT_OF_BOUNDS":
                slist[l].append("FAILURE")
            
    return slist