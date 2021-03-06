import MusicFiles

class Artist:
    """A class representing a particular artist within a Library"""
    
    def __init__(self, name):
        self.name = name
        self.albums = []
    
    def add_album(self, name):
        """Puts a new Album into the artist from a string name.
        
        To be called by the class after checking that the album isn't
        already in here. Returns the new Album object.
        """
        new = Album(name)
        self.albums.append(new)
        return new
        
    def album_from_str(self, name):
        """Given the name of an album as a string, returns the Album.
        
        If that album isn't here, returns false.
        """        
        for a in self.albums:
            if a.name = name:
                return a
        return False
    
    def add_file(self, file):
        """Adds a MusicFile to this artist.
        
        If necessary, adds the Album to the Artist. then passes the file
        on to the album in question.
        Returns 0 if everything went well. If the track already existed 
        in that format, returns 1.
        """
        album = self.album_from_str(file.album)
        if not album: #ie, if it returned false b/c album not here yet
            album = self.add_album(file.album)
        #When we get here album is most definitely the Album
        return album.add_file(file)
    
        
