import MusicFiles

class Track:
    """A class representing a particular Track within an Album.
    
    A track contains one or more formats. The formats it contains are 
    the formats this track exists in within the library.
    """
    
    def __init__(self, name):
        self.name = name
        self.files = []
        
    def has_format(self, format):
        """Returns whether or not this track exists under the format"""
        for f in self.formats:
            if f==format:
                return True
        return False
    
    def add_file(self, file):
        """Adds a MusicFile to this Track.
        
        Returns 0 if everything went well. If the track already existed 
        in that format, returns 1.
        """
        for f in self.files:
            if file.getFullFormat()==f.getFullFormat():
                return 1
        # If we get here, the new file does not match any formats we 
        # already have
        self.files.append(file)
        return 0