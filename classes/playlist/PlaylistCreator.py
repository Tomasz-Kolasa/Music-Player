from .PlaylistItem import PlaylistItem
import random

class PlaylistCreator:
    def __init__(self, playlistOperator):
        self.playlistOperator =  playlistOperator


    def createPlaylistWithUser(self):
        self.playlistOperator.player.albumsReader.printAlbums()
        while(True):
            selection = input("Select album and song in [Album Number,Song Number] format. Hit Enter to finish\n")
            if selection=='':
                break
            if self.isInputValidSongSelection(selection):
                albumNumber = int(selection.split(',')[0])
                songNumber = int(selection.split(',')[1])
                self.playlistOperator.addItemToPlaylist( PlaylistItem(albumNumber,songNumber) )
            else:
                print(f"'{selection}' is not a valid choice!")
    
    def isInputValidSongSelection(self, selection)->bool:
        songCoordinates = selection.split(',')
        if( 2 == len(songCoordinates) ):
            try:
                albumNumber = int(songCoordinates[0])
                songNumber = int(songCoordinates[1])
            except ValueError:
                return False

            if( self.playlistOperator.player.albumsReader.isSongExists(albumNumber, songNumber) ):
                return True
            else:
                return False
        else:
            return False

