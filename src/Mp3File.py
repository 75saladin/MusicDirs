from mutagen.easyid3 import EasyID3
from mutagen import File

class Mp3File(LossyMusicFile):
    """A class representing an mp3 file."""
    
    bitrates = [32000, 40000, 48000, 56000, 64000, 80000, 96000, 112000, 
                128000, 160000, 192000, 224000, 256000, 320000, 999999]
    
    def parseBitrate(br):
        prevDiff=9999999
        for std in bitrates:
            diff = abs(br-std)
            if diff>prevDiff:
                return prev
            prevDiff = diff
            prev = std        
            
        
    def __init__(self, location):
        super().__init__(location)
        
        id3Info = EasyID3(location)
        self.artist = id3Info['artist'][0]
        self.album = id3Info['album'][0]
        self.title = id3Info['title'][0]
        self.bitrate = parseBitrate(File(location).info.bitrate)