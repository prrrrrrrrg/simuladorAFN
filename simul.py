def simulation(sdict,afn,user_input,state_cursor,input_cursor,branch_no):
    if not state_cursor in afn["transicoes"][user_input[input_cursor]]: #if there are no transitions
        sdict[branch_no].append(str(input_cursor) + " (" + str(user_input[input_cursor]) + "): CRASHED") #add crash report
        print("[" + str(branch_no) + "] " + str(sdict[branch_no])) #print that motherfucker
    else:
        for i in range(len(afn["transicoes"][user_input[input_cursor]][state_cursor])): #for each possible transition
            if not i == 0: #if it's a second transition or more, create a new branch
                branch_no = branch_no + 1
            new_state = afn["transicoes"][user_input[input_cursor]][state_cursor][i] #check the destination state
            if not branch_no in sdict: #if a new branch has been created, set as list
                sdict[branch_no] = []
            sdict[branch_no].append(str(input_cursor) + " (" + str(user_input[input_cursor]) + "): " + str(state_cursor) + " -> " + str(new_state)) #add list entry to the transition
            print("[" + str(branch_no) + "] " + str(sdict[branch_no])) #print that motherfucker
            if input_cursor + 1 >= len(user_input):
                if new_state in afn["finais"]:
                    sdict[branch_no].append(str(input_cursor) + " (" + str(user_input[input_cursor]) + "): SUCCESS") #add success report
                    print("[" + str(branch_no) + "] " + str(sdict[branch_no])) #print that motherfucker
                    break
                else:
                    sdict[branch_no].append(str(input_cursor) + " (" + str(user_input[input_cursor]) + "): FAILURE") #add failure report
                    print("[" + str(branch_no) + "] " + str(sdict[branch_no])) #print that motherfucker
                    break
            simulation(sdict, afn, user_input, new_state, input_cursor + 1, branch_no) #simulate the next transition