import sys
from eVotUM.Cripto import eccblind

def printUsage():
    print("Usage: python initSigner-app.py [-init]")

def parseArgs():
    if (len(sys.argv) > 2):
        printUsage()
    else:
        main()

def main():
    initComponents, pRDashComponents = eccblind.initSigner()
    if (len(sys.argv) == 1):
        print("Output")
        #print("Init components: %s" % initComponents)
        print("pRDashComponents: %s" % pRDashComponents)
    elif(len(sys.argv) == 2 and sys.argv[1] == '-init'):
        file = open('init_Sig.txt','w+')
        file.write(initComponents +' \n' + pRDashComponents+' \n')
        file.close()
        print ("Components saved in init_Sig.txt")


if __name__ == "__main__":
    parseArgs()
