from mutagen.easyid3 import EasyID3
from mutagen import File

class MusicFile:
    """A class representing a particular music file."""
    
    def __init__(self, location):
        self.location = location

###############################################################################        

class LosslessMusicFile(MusicFile):
    """"""
    def __init__(self, location):
        super().__init__(location)

###############################################################################
        
class LossyMusicFile(MusicFile):
    """"""
    def __init__(self, location):
        super().__init__(location)
        
    def parseBitrate(br):
        """Takes a given precise bitrate value and rounds it to the closest
        standard bitrate.
        
        Standard bitrate varies by specific filetype and it to be set by the 
        child.
        """
        prevDiff=999999999
        for std in self.bitrates:
            diff = abs(br-std)
            if diff>prevDiff:
                return prev
            prevDiff = diff
            prev = std
        

###############################################################################
        
class FlacFile(LosslessMusicFile):
    """A class representing a FLAC file."""
    
    def __init__(self, location):
        super().__init__(location)
        
        self.artist = File(location)['artist'][0]
        self.album = File(location)['album'][0]
        self.title = File(location)['title'][0]

###############################################################################
        
class Mp3File(LossyMusicFile):
    """A class representing an mp3 file."""
    
    bitrates = (32000, 40000, 48000, 56000, 64000, 80000, 96000, 112000, 
                128000, 160000, 192000, 224000, 256000, 320000, 999999)
        
    def __init__(self, location):
        super().__init__(location)
        
        id3Info = EasyID3(location)
        self.artist = id3Info['artist'][0]
        self.album = id3Info['album'][0]
        self.title = id3Info['title'][0]
        self.bitrate = parseBitrate(File(location).info.bitrate)