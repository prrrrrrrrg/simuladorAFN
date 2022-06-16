import read
import simul
import os
import sys

sys.tracebacklimit = 0

here = os.path.dirname(os.path.abspath(__file__))
if os.path.exists(os.path.join(here,"input.txt")):
    afn = read.getAFN("input.txt")
else:
    while(True):
        file_path = input("Por favor digite o caminho até o arquivo nesta pasta: ")
        if os.path.exists(os.path.join(here,file_path)):
            print("")
            afn = read.getAFN(file_path)
            break
        print("Arquivo não encontrado no caminho recebido.\n")


for u in afn["alfabeto"]:
    if not u == "epsilon":
        if len(u) > 1:
            print("O seu alfabeto contém entrada com mais de um caractére.")
            print("Em casos desse tipo, por favor utilize virgulas ao digitar a sua cadeia de entrada.\n")
user_input = input("\nInsira sua cadeia de entrada: ")
if "," in user_input:
    user_input = read.strCleanup(user_input,1)
else:
    user_input = read.strCleanup(user_input,2)
for i in user_input:
    if not i in afn["alfabeto"]: raise Exception("Utilizou alfabeto na cadeia de entrada diferente do definido.")

slist = simul.simulation(afn,user_input)
for entry in range(len(slist)):
    print(slist[entry])