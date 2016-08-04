import MusicFiles

class Artist:
    """A class representing a particular artist within a Library"""
    
    def __init__(self, name):
        self.name = name
        self.albums = []
    
    def getName(self):
        return self.name
        
    def addAlbum(self, name):
        """Puts a new Album into the artist from a string name.
        
        To be called by the class after checking that the album isn't already 
        in here. Returns the new Album object.
        """
        new = Album(name)
        self.albums.append(new)
        return new
        
    def getAlbum(self, name):
        """Given the name of an album as a string, returns the Album.
        
        If that album isn't here, returns false.
        """        
        for a in self.albums:
            if a.getName() = name:
                return a
        return False
    
    def addFile(self, file):
        """Adds a MusicFile to this artist.
        
        If necessary, adds the Album to the Artist. then passes the file on 
        to the album in question.
        Returns 0 if everything went well. If the track already existed in that
        format, returns 1.
        """
        album = self.getAlbum(file.getAlbum())
        if not album: #ie, if it returned false b/c album not here yet
            album = self.addAlbum(file.getAlbum())
            
        #When we get here album is most definitely the Album
        return album.addFile(file)
    
        
