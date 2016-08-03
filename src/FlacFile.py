from mutagen import File

class FlacFile(LosslessMusicFile):
    """A class representing a FLAC file."""
    
    def __init__(self, location):
        super().__init__(location)
        
        self.artist = File(location)['artist'][0]
        self.album = File(location)['album'][0]
        self.title = File(location)['title'][0]