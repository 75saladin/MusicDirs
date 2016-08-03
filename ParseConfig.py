import sys
import re
import os
from pathlib import Path

configsLocation = os.path.dirname(__file__)+"use/"
configArgIndex = 1
useFlags = ["--help", "--use", "-h", "-u"]
usageText="Use "+useFlags.__str__()+" to invoke this usage text.\n\nGive the name of a config file located in use/, with or without the trailing '.txt' and leading 'use/', to apply to the program's operations."
    
def parseCmd():
    """Parses and processes command-line arguments.
    
    Currently handles useFlags or config file specfication.
    Returns logical representation of the music directory structure if one is given.
    """

    flaged = False
    for arg in sys.argv:
        #ie, if it's the program name
        if arg.endswith(".py"):
            continue
        
        #If arg matches one of useFlags, print usage and return
        for f in useFlags:
            if f==arg: 
                print(usageText)
                return None
            
        #If we get here, it's a config file
        confArg = arg 
        if not confArg.endswith(".txt"):
            confArg = arg+".txt"
        if confArg.startswith("use/"):
            confArg = confArg[4:]
            
        f = open(configsLocation+confArg)
        theThingToReturn = parseConfig(f)
    
    #If we get here, args are done with no early returns. Return the thing.
    return theThingToReturn

def parseConfig(f):
    """Parses the file into a meaningful dictionary.
    
    Example of returned dictionary: {'scheme': '%artist%/%album%/', 'cbase': 
    '/media/Storage/Music/archive', 'formats': {'mp3/320': 'portable/', 'flac':
    'flac/', 'mp3/192': 'portable190/'}}
    """
    config = {"formats":{}}
    
    for line in f:
        if line.startswith("//"): 
            continue
        
        sline = re.split("[=\s]", line)
        if sline[0] is "":
            continue
        
        if sline[0]=="format":
            #Puts the format as a key in the dict pointed to by "formats"
            config["formats"][sline[1]] = sline[3]                
        else:
            config[sline[0]] = sline[1]
            
    return config

###############################################################################

config = parseCmd()
if config is not None:
    print(config)
else:
    print("Not moving on")