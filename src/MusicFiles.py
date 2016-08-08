from mutagen.easyid3 import EasyID3
from mutagen import File

class MusicFile(object):
    """A class representing a particular music file.
    
    Children that are intended to be instantiated must initialize fields
    for the getters that exist in this class.
    """
    
    def __init__(self, location):
        self.location = location

###############################################################################       


class LosslessMusicFile(MusicFile):
    """A class representing a lossless music file.
    
    Contains all functionality required only by only lossless music 
    files. To date, that is only returning full format more plainly 
    than do lossy files.
    """
    def __init__(self, location):
        super().__init__(location)
        
    def full_format(self):
        return self.format       
    
###############################################################################

        
class LossyMusicFile(MusicFile):
    """A class representing a lossy music file.
    
    Contains all functionality required by only lossy music files. To 
    date, that is processing bitrates into a standard number and 
    returning format with bitrate.
    """
    def __init__(self, location):
        super().__init__(location)
        
    def parse_bitrate(self, br):
        """Takes a given precise bitrate value and rounds it to the 
        closest standard bitrate.
        
        Standard bitrate varies by specific filetype and is to be set by
        the child.
        """
        prevdiff=999999999
        for std in self.bitrates:
            # As we iterate through the ordered list, difference should 
            # be getting smaller and smaller as we tend towards the best
            # rounding value. When the difference gets bigger, we know 
            # the previous one was the closest.
            diff = abs(br-std)
            if diff>prevdiff:
                return prev
            prevdiff = diff
            prev = std
    
    def full_formatt(self):
        """Return the format as a tuple, format string followed by 
        bitrate.
        """
        return (self.format, str(self.bitrate))

###############################################################################

        
class FlacFile(LosslessMusicFile):
    """A class representing a FLAC file."""
    format = "FLAC"
    
    def __init__(self, location):
        super().__init__(location)
        self.artist = File(location)['artist'][0]
        self.album = File(location)['album'][0]
        self.title = File(location)['title'][0]

###############################################################################

        
class Mp3File(LossyMusicFile):
    """A class representing an mp3 file."""
    format = "mp3"
    # Threw a large value on the end so parseBitrate() can iterate after
    # the end
    bitrates = (
        32000, 40000, 48000, 56000, 64000, 80000, 96000, 112000, 128000, 
        160000, 192000, 224000, 256000, 320000, 999999
    )
        
    def __init__(self, location):
        super().__init__(location)
        id3Info = EasyID3(location)
        self.artist = id3Info['artist'][0]
        self.album = id3Info['album'][0]
        self.title = id3Info['title'][0]
        # Once we set it here, bitrate shall be known in kbps
        self.bitrate = int((self.parse_bitrate(File(location).info.bitrate))/1000)