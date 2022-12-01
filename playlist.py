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

  def shuffle(self):
    if len(self.__tracks) > 1:
      self.__tracks = deque(sorted(self.__tracks, key=lambda k: random()))
      print('Playlist shuffled.')
    else:
      print("The playlist is too short to shuffle.")
      
  def playNext(self):
    if len(self.__tracks) > 1:
      self.__tracks.rotate(1)
      self.__current_track = self.__tracks[0]
      print(f'Now playing: {self.__current_track}')
      return self.__current_track
    else:
      print("Cannot play next track.")
      
  def playPrevious(self):
    if len(self.__tracks) > 1:
      self.__tracks.rotate(-1)
      self.__current_track = self.__tracks[0]
      print(f"Now playing: {self.__current_track}')
      return self.__current_track
    else:
      print("Cannot play previous track.")
     
  def repeat(self):
    if len(self.__tracks) > 0:
            print(f'Now playing: {self.__current_track}')
            return self.__current_track
    else:
            print("Cannot repeat track.")
