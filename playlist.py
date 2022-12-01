class Playlist:
  def __init__(self, name, length):
    self.__name = name
    self.__tracks = deque(maxlen=length)
    seld.__current_track = None 
    
  def addtrack (self, track):
    self.__tracks.append(track)
    if self.__current_track is None:
      self.__current_track = track
      print(f'Now playing: {self.__current_track}')
    else:
      print(f'{track} added to the playlist.')
      print('You have {} track(s) in your playlist.'.format(len(self.__tracks)))
      
      return True
    return False
