import sys
import re
import os
from pathlib import Path

configsLocation = os.path.dirname(__file__)+"use/"
configArgIndex = 1
    
def parseCmd(cmdArg):
    """Takes the cmdline config name, turns it into a file, and passes it on.
    """
    if not cmdArg.endswith(".txt"):
        cmdArg+=".txt"
    f = open(configsLocation+cmdArg)
    return parseConf(f)

def parseConf(f):
    """Parses the file into meaningful stuff.
    
    Example of returned dictionary: {'scheme': 'artist/album/', 'cbase': 
    '/media/Storage/Music/archive', 'formats': {'mp3/320': 'portable/', 'flac':
    'flac/', 'mp3/192': 'portable190/'}}
    """
    config = {"formats":{}}
    formats = {}
    
    for line in f:
        if line.startswith("//"): 
            continue
        sline = re.split("[=\s]", line)
        if sline[0]!="":
            if sline[0]=="format":
                config["formats"][sline[1]]=sline[3]                
            else:
                config[sline[0]] = sline[1]
    return config

config = parseCmd(sys.argv[configArgIndex])
print(config)