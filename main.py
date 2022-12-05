from playlist import Playlist
from track import Track

def main():
  while True:
    print("Welcome to the next episode of the biggest hit tracklist show.")
    MainMenu = input('***Press:***\n'
                    '1 - Create a new playlist\n'
                    '2 - Add a track at the end of the playlist\n'
                    '3 - Play the next track\n'
                    '4 - Play the previous track\n'
                    '5 - Repeat the current track\n'
                    '6 - Remove a track from the playlist\n'
                    '7 - Display the playlist\n'
                    '8 - Shuffle the playlist\n'
                    '0 - Quit\n')
    if MainMenu =='1':
          UserName = input('Enter your name: ')
          playlist = Playlist(UserName, 20 ) 
          print(f"Playlist created for {UserName}.")
          print(playlist)
          
    elif MainMenu == '2':
          TrackTitle = input('Enter the track title: ')
          TrackArtist = input('Enter the track artist: ')
          track = Track(TrackTitle, TrackArtist)
        try: 
               playlist.addTrack(track)
        except NameError:
               print('Please create a playlist first.')
            
    elif MainMenu == '3':
        try: 
            playlist.playNext()
        except NameError:
              print('Please create a playlist first.')
            
    elif MainMenu == '4':
        try:
            playlist.playPrevious()
        except NameError:
              print('Please create a playlist first.')
            
    elif MainMenu == '5':
        try: 
             playlist.repeat()
        except NameError:
              print('Please create a playlist first.')
            
    elif MainMenu == '6':
        trackToRemove = input('Enter the track to remove: ')
        try:
            playlist.removeTrack(trackToRemove)
        except NameError:
            print('Please create a playlist first.')
                
    elif MainMenu == '7':
        print(playlist)
                  
    elif MainMenu == '8':
        try:
            playlist.shuffle()
        except NameError:
            print('Please create a playlist first.')
                    
    elif MainMenu == '0':
        break
      
    else:
      print('Invalid input.')
      
      
if__name__=='__main__':
  main()
