# open input file
input = open("/home/prrg/TC/simuladorAFN/input.txt", "r")
afn = {}

while (True):
    str = input.readline()
    if "alfabeto=" in str:
        cleanStr = str.replace("alfabeto=","")
        cleanStr = cleanStr.replace("\n","")
        cleanStr = cleanStr.replace(" ","")
        afn["alfabeto"] = cleanStr.split(",")
        print(afn["alfabeto"])
    if "estados=" in str:
        cleanStr = str.replace("estados=","")
        cleanStr = cleanStr.replace("\n","")
        afn["estados"] = cleanStr.split(",")
        print(afn["estados"])
    if "inicial=" in str:
        cleanStr = str.replace("inicial=","")
        cleanStr = cleanStr.replace("\n","")
        cleanStr = cleanStr.replace(" ","")
        afn["inicial"] = cleanStr
        print(afn["inicial"])
    if "finais=" in str:
        cleanStr = str.replace("finais=","")
        cleanStr = cleanStr.replace("\n","")
        cleanStr = cleanStr.replace(" ","")
        afn["finais"] = cleanStr.split(",")
        print(afn["finais"])
    if not str:
        break