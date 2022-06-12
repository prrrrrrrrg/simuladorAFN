# open input file
input = open("/home/prrg/TC/input.txt", "r")
afn = {}

str = input.readline()
if "alfabeto=" in str:
    cleanStr = str.replace("alfabeto=","")
    cleanStr = cleanStr.replace(" ","")
    afn["alfabeto"] = cleanStr.split(",")
    print(afn["alfabeto"])