import MusicFiles

class Library:
    """The object that represents an entire music library of one or more
    formats"""
    def __init__(self, loc):
        self.location = loc
        self.artists = []
        
        
    def add_artist(self, name):
        """Puts a new Artist into the library from a string name.
        
        To be called by the class after checking that the artist isn't 
        already in here. Returns the new Artist object.
        """
        new = Artist(name)
        self.artists.append(new)
        return new
        
    def artist_from_str(self, name):
        """Given the name of an artist as a string, returns the Artist.
        
        If that artist isn't here, returns false.
        """        
        for a in self.artists:
            if a.name = name:
                return a
        return False
    
    def add_file(self, file):
        """Adds a MusicFile to this library.
        
        If necessary, adds the artist to the library. then passes the 
        file on to the artist in question.
        Returns 0 if everything went well. If the track already existed 
        in that format, returns 1.
        """
        artist = self.artist_from_str(file.artist)
        if not artist: #ie, if it returned false b/c artist not here yet
            artist = self.add_artist(file.artist)
        #When we get here artist is most definitely the Artist
        return artist.add_file(file)
        
        
        
        
        
            