from tracklist import Tracklist
from track import Track

def main():
  while True:
    print("Welcome to the next episode of the biggest hit tracklist show.")
    MainMenu = input('***Press:***\n'
                    '1 - Create a new tracklist\n'
                    '2 - Add a track at the start of the tracklist\n'
                    '3 - Add a track at the end of the tracklist\n'
                    '4 - Play the next track\n'
                    '5 - Play the previous track\n'
                    '6 - Repeat the current track\n'
                    '7 - Remove a track from the tracklist\n'
                    '8 - Display the tracklist\n'
                    '9 - Shuffle the tracklist\n'
                    '0 - Quit\n')
    if MainMenu =='1':
          UserName = input('Enter your name: ')
          tracklist = Tracklist(UserName, 20 ) 
          print(f"Playlist created for {UserName}.")
          print(tracklist)
          
          
    elif MainMenu == '2':
			    TrackTitle = input('Enter the song title: ')
			    TrackArtist = input('Enter the song artist: ')
			    track = Track(TrackTitle, TrackArtist)
			try:
				       tracklist.addTracktoFirst (track)
			except NameError:
				        print('Please create a tracklist first.')
    elif MainMenu == '3':
          TrackTitle = input('Enter the track title: ')
          TrackArtist = input('Enter the track artist: ')
          track = Track(TrackTitle, TrackArtist)
        try: 
               tracklist.addTracktoLast(track)
        except NameError:
               print('Please create a tracklist first.')
            
    elif MainMenu == '4':
        try: 
            tracklist.playNext()
        except NameError:
              print('Please create a tracklist first.')
            
    elif MainMenu == '5':
        try:
            tracklist.playPrevious()
        except NameError:
              print('Please create a tracklist first.')
            
    elif MainMenu == '6':
        try: 
             tracklist.repeat()
        except NameError:
              print('Please create a tracklist first.')
            
    elif MainMenu == '7':
        trackToRemove = input('Enter the track to remove: ')
        try:
            tracklist.removeTrack(trackToRemove)
        except NameError:
            print('Please create a tracklist first.')
                
    elif MainMenu == '8':
        print(tracklist)
                  
    elif MainMenu == '9':
        try:
            tracklist.shuffle()
        except NameError:
            print('Please create a tracklist first.')
                    
    elif MainMenu == '0':
        break
      
    else:
      print('Invalid input.')
      
      
if__name__=='__main__':
  main()
