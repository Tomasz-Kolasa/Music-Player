from albums.albums import *
from classes.Player import Player

print("Let's create a playlist!")
player = Player( albums )
player.createPlaylistWithUser()

#print(player.playlistCreator.playlist.shuffleHistory)

while(True):
    print("\nWhat would you like to do now?")
    print(" 1 - show playlist")
    print(" 2 - shuffle playlist")
    print(" 3 - play")
    print(" 4 - remove song from playlist")
    print("Press Enter to exit")
    choice = input()

    if '1' == choice:
        player.printPlaylist()
    elif '2' == choice:
        try:
            player.shuffle()
        except Exception as exception:
            print(exception)
    elif '3' == choice:
        try:
            player.play()
        except Exception as exception:
            print(exception)
    elif '4' == choice:
        player.removeSongWithUser()
    elif '' == choice:
        print("Bye!")
        break
    else:
        print(f"\n'{choice}' is not an option!")