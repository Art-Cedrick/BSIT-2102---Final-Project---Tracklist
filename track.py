class Track:
  
  def __init__(self, title, artist):
    self.__title = title
    self.__artist = artist
    
  def get_title(self):
    return self.__title
  
  def get_artist(self):
    return self.__artist
  
  def __str__(self):
    return '\"{}\" by {}\n'.format(self.__title, self.__artist)
  
  def __eq__(self, other):
    return self.__title == other.get_title() \
           and self.__artist == other.get_artist()
