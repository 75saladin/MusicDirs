# MusicDirs

src/ contains source files.
use/ contains stuff the user should edit, like config files. If you tell the
     program to use a filename that exists here, it will be hip to that.

2016/07/31: 
  Initial commit. The goal of this project is to manage my music library between
  two, and possibly an arbitrary number of, formats and locations. This will 
  involve navigating the directories to find what albums are in common and which
  aren't. When one exists in a higher (ie, closer to lossless) format but not a
  lower format, it will be converted, sorted, and moved appropriately in order
  to facilitate my laziness. When one exists in a lower format but not in a
  higher one, that will be made note of and promptly never be looked at. Right
  now my idea is to use plain-text config files, supplied on the command-line,
  to allow the user to specify sets of options and swap between them simply by
  specifying a different config file.
  
  Final commit: ParseConfig takes one argument: the name of a config file in 
  use/, with or without .txt extension, from which the music directories schema
  will be generated. Currently the schema will simply be printed. Still needed:
  a self-contained explanation. Probably a --use flag which will just contain 
  this info. Next to tackle: delving into the music directories and comparing 
  their contents. That won't be very useful (unless I have some albums that are
  missing tracks), but it will once I get into reading the tags and and 
  operating based on that.