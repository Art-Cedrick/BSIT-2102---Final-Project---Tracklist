class Track:
  
  def __init__(self, title, artist):
    """
    Initializes the song.
    
    """
    self.__title = title
    self.__artist = artist
    
  def get_title(self):
    """
    Returns the title of the song.
    
    """
    return self.__title
  
  def get_artist(self):
    """
    Returns the artist of the song.
    
    """
    return self.__artist
  
  def __str__(self):
    """
    Returns the string representation of the song.
    
    """
    return '\"{}\" by {}\n'.format(self.__title, self.__artist)
