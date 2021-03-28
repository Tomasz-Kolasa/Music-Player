from .Playlist import Playlist
from .PlaylistItem import PlaylistItem
from classes.AlbumsReader import AlbumsReader

class PlaylistSongRemover:
    def __init__(self, playlistOperator):
        self.playlistOperator =  playlistOperator


    def removeSongWithUser(self):
        self.playlistOperator.printPlaylist()
        while(True):
            userInput = input("Enter song number or hit ENTER to cancel\n")
            if '' == userInput:
                return
            try:
                userPickedNumber = int(userInput)
            except ValueError:
                self.informUserInvalidChoice(userInput)
                continue

            playlistItemsQty = len( self.playlistOperator.playlist.playlistItems )
            if 0==playlistItemsQty:
                print("\nPlaylist empty.")
                break

            if userPickedNumber in range(1, playlistItemsQty+1):
                itemListIndex = userPickedNumber-1

                properIndex = self.getRelevantIndexConsideringShuffle(itemListIndex)
                self.playlistOperator.removeItemFormPlaylist( properIndex )
                print("\nSong removed.")
                break
            else:
                self.informUserInvalidChoice(userInput)


    def informUserInvalidChoice(self, userInput):
        print(f"\n{userInput} is not a an option!")


    def getRelevantIndexConsideringShuffle(self,index:int)->int:
        currentShuffleOrder = self.playlistOperator.playlistShuffler.shuffleHistory[-1]
        indexOfItemOnPlaylistItems = currentShuffleOrder[index]
        return indexOfItemOnPlaylistItems
        
        