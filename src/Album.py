import MusicFiles

class Album:
    """A class representing a particular album within an Artist"""
    
    def __init__(self, name):
        self.name = name
        self.tracks = []
        
    def getName(self):
        return self.name
        
    def addTrack(self, name):
        """Puts a new Track into the album from a string name.
        
        To be called by the class after checking that the track isn't already 
        in here. Returns the new Track object.
        """
        new = Track(name)
        self.tracks.append(new)
        return new
    
    def getTrack(self, name):
        """Given the name of a track as a string, returns the Track.
        
        If that track isn't here, returns false.
        """        
        for t in self.tracks:
            if t.getName() = name:
                return t
        return False
    
    def addFile(self, file):
        """Adds a MusicFile to this album.
        
        If necessary, adds the Track to the Album. then passes the file on 
        to the Track in question.
        Returns 0 if everything went well. If the track already existed in that
        format, returns 1.
        """
        track = self.getTrack(file.getTrack())
        if not track: #ie, if it returned false b/c track not here yet
            track = self.addTrack(file.getTrack())
            
        #When we get here track is most definitely the Track
        return track.addFile(file)