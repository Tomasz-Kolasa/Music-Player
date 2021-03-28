from .PlaylistCreator import PlaylistCreator
from .PlaylistSongRemover import PlaylistSongRemover
from .Playlist import Playlist
from .PlaylistShuffler import PlaylistShuffler
from .PlaylistItem import PlaylistItem

class PlaylistOperator:
    def __init__(self, player):
        self.player =  player
        self.playlist = Playlist()
        self.playlistCreator = PlaylistCreator( self )
        self.playlistSongRemover = PlaylistSongRemover( self )
        self.playlistShuffler = PlaylistShuffler(self.playlist)


    def addItemToPlaylist(self, playlistItem:PlaylistItem):
        self.playlist.addItem(playlistItem)
        self.playlistShuffler.resetShuffleHistory()


    def removeItemFormPlaylist(self, index:int):
        self.playlist.removeItem(index)
        self.playlistShuffler.resetShuffleHistory()


    def shuffle(self):
        self.playlistShuffler.shuffle()
        print("Shuffled")


    def createPlaylistWithUser(self):
        self.playlistCreator.createPlaylistWithUser()


    def removeSongWithUser(self):
        self.playlistSongRemover.removeSongWithUser()

    
    def printPlaylist(self):
        playlistItemsQty = len( self.playlist.playlistItems )
        if(0==playlistItemsQty):
            print("\nPlaylist empty!")
            return

        playOrderList = self.playlistShuffler.shuffleHistory[-1]

        for (index, positionOnPlaylist) in enumerate(playOrderList, start=1):
            playlistItem = self.playlist.playlistItems[positionOnPlaylist]
            song = self.player.albumsReader.getSongByAlbumNoAndSongNo(
                playlistItem.albumNumber, playlistItem.songNumber)
            print(f"    {index}: From album {song.album}: {song.artist} - {song.title}")