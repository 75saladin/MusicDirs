class Track:
    """A class representing a particular Track within an Album.
    
    A track contains one or more formats. The formats it contains are the 
    formats this track exists in within the library.
    """
    
    def __init__(self, name):
        self.name = name
        self.formats = []
        
    def addFormat(format):
        """Adds a format to this track.
        
        To be called by this class after checking if the track already has the
        format.
        """
        self.formats.append(format)
    
    def hasFormat(format):
        """Returns whether or not this track exists under the format"""
        for f in self.formats:
            if f==format:
                return True
        return False
    
    def addFile(file):
        """Adds a MusicFile to this Track.
        
        Returns 0 if everything went well. If the track already existed in that
        format, returns 1.
        """
        
        if self.formats has file.format:
            return 1
        self.addFormat(file.format)
        return 0