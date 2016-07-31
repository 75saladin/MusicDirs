A config file should be a .txt file. It should contain one or more lines. The most basic lines are simply an identifier, followed by an equals sign (=), followed by a directory to assign to that identifier. For example:

foo=/example/directory
bar=/Pictures/2016Vacation

However, "foo" and "bar" are not legitimate identifiers. Here is a list of identifiers and their meanings:

- "cbase": defines the common directory where music is stored. For example, I keep my music in media/lucas/Storage/Music/archive, so my "cbase" line would be "cbase=/media/lucas/Storage/Music/archive". In that archive folder, I have subfolders that separate the formats, but that will be specified later.
- "scheme": defines the scheme for organizing music files into their locations. Putting a word between % symbols will cause that phrase to be replaced with specific information about the music files that are being organized. We call these phrases "tags". For example, I like my music organized into one folder for each artist, then subfolders for each album. So my line would be "scheme=%artist%/%album%". Here we used the artist tag and the album name tag. This artist, album, and other information about the music will always be taken from the ID3 tags of the music. Here is a list of tags we use:
    - %artist%: Artist
    - %album%: Album name

Finally, we must specify what formats we will be storing the music in. This is acheived by using a "format" identifier followed by a "base" identifier. The "format" identifier defines what the format is, and the "base" identifier gives the location where music of that format should be, relative to the cbase you have defined. Here is an example:

format=wav base=my_wav_music/

So, assuming I'm using a cbase of media/lucas/Storage/Music/archive, then my wav music is located in media/lucas/Storage/Music/archive/my_wav_music. Assuming I have a scheme set up, my wav music will be under media/lucas/Storage/Music/archive/my_wav_music/[artist name]/[album name]. You may include any number of format lines for as many formats as you need to manage. IF the format information needs further specification (such as bitrate), simply include it after a forward slash, like this:

format=mp3/320 base=music_for_my_special_ears/

The order of lines in a config file is not considered.
Finally, any line starting with "//" will be completely ignored by the program. See "exampleConfig.txt" for an example that may be easier to understand than these instructions.


