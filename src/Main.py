import sys
from pathlib import Path

configArgIndex = 1

def parseCmd(cmdArg):
    print("Trust me, I'm parsing "+cmdArg)
    cmdArg+=".txt"
    parseConf(cmdArg)

def parseConf(filename):
    print("Don't believe that dingus, I'M parsing "+filename)
    
print("Hello World!")
parseCmd(sys.argv[configArgIndex])
print("Those guys are expert parsers, huh? Bye-bye")