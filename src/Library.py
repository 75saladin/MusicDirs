import MusicFiles

class Library:
    """The object that represents an entire music library of one or more formats"""
    def __init__(self, loc):
        self.loc = loc
        self.artists = []
        
    def printRoot(self):
        print(loc)
        
    def addArtist(self, name):
        """Puts a new Artist into the library from a string name.
        
        To be called by the class after checking that the artist isn't already 
        in here. Returns the new Artist object.
        """
        new = Artist(name)
        self.artists.append(new)
        return new
        
    def getArtist(self, name):
        """Given the name of an artist as a string, returns the Artist.
        
        If that artist isn't here, returns false.
        """        
        for a in self.artists:
            if a.getName() = name:
                return a
        return False
    
    def addFile(self, file):
        """Adds a MusicFile to this library.
        
        If necessary, adds the artist to the library. then passes the file on 
        to the artist in question.
        Returns 0 if everything went well. If the track already existed in that
        format, returns 1.
        """
        artist = self.getArtist(file.getArtist())
        if not artist: #ie, if it returned false b/c artist not here yet
            artist = self.addArtist(file.getArtist())
            
        #When we get here artist is most definitely the Artist
        return artist.addFile(file)
        
        
        
        
        
            