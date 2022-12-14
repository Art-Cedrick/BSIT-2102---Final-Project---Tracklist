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
                    '7 - Display the tracklist\n'
                    '8 - Shuffle the tracklist\n'
                    '0 - Quit\n')
    if MainMenu =='1': # Creating a new tracklist
          UserName = input('Enter your name: ')
		# 20 is the amount of sos one can put on the tracklist to
		# demonstrate the functionality of the program using a deque.
          tracklist = Tracklist(UserName, 20 ) 
          print(f"Playlist created for {UserName}.")
          print(tracklist)
          
          
    elif MainMenu == '2': # Adding a track at the beginning of the tracklist
			    TrackTitle = input('Enter the song title: ')
			    TrackArtist = input('Enter the song artist: ')
			    track = Track(TrackTitle, TrackArtist)
			try:
				       tracklist.addTracktoFirst (track)
			except NameError:
				        print('Please create a tracklist first.')
    elif MainMenu == '3': # Adding a track at the end of the tracklist
          TrackTitle = input('Enter the track title: ')
          TrackArtist = input('Enter the track artist: ')
          track = Track(TrackTitle, TrackArtist)
        try: 
               tracklist.addTracktoLast(track)
        except NameError:
               print('Please create a tracklist first.')
            
    elif MainMenu == '4': # To play the next track
        try: 
            tracklist.playNext()
        except NameError:
              print('Please create a tracklist first.')
            
    elif MainMenu == '5': # To play the previous track
        try:
            tracklist.playPrevious()
        except NameError:
              print('Please create a tracklist first.')
            
    elif MainMenu == '6': # To repeat the current track
        try: 
             tracklist.repeat()
        except NameError:
              print('Please create a tracklist first.')
            
    
                
    elif MainMenu == '7': # To display the whole tracklist
        print(tracklist)
                  
    elif MainMenu == '8': # To shuffle the playlist
        try:
            tracklist.shuffle()
        except NameError:
            print('Please create a tracklist first.')
                    
    elif MainMenu == '0': # Exit
        break
      
    else:
      print('Invalid input.') # User input were out of the choices
      
      
if__name__=='__main__':
  main()
