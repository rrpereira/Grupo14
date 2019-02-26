import sys
from eVotUM.Cripto import eccblind


def printUsage():
    print("Usage: python ofusca-app.py -msg <mensagem a assinar> -RDash <pRDashComponents>")

def parseArgs():
    if (len(sys.argv) != 5):
        printUsage()
    elif (sys.argv[1] != '-msg' or sys.argv[3] != '-RDash'):
        printUsage()
    else:
        main()

def showResults(errorCode, result):
    print("Output")
    if (errorCode is None):
        blindComponents, pRComponents, blindM = result
        print("Blind message: %s" % blindM)
        file = open('Blind_Components.txt',"w+")
        file.write(blindComponents+'\n'+pRComponents)
        file.close()
    elif (errorCode == 1):
        print("Error: pRDash components are invalid")

def main():
    data = sys.argv[2]
    pRDashComponents = sys.argv[4]
    errorCode, result = eccblind.blindData(pRDashComponents, data)
    showResults(errorCode, result)

if __name__ == "__main__":
    parseArgs()
