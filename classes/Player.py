from .AlbumsReader import AlbumsReader
from .playlist.PlaylistOperator import PlaylistOperator

class Player:
    def __init__(self, albums:list):
        self.albums = albums
        self.albumsReader = AlbumsReader(self.albums)
        self.playlistOperator = PlaylistOperator(self)

    def shuffle(self):
        self.playlistOperator.shuffle()


    def createPlaylistWithUser(self):
        self.playlistOperator.createPlaylistWithUser()


    def printPlaylist(self):
        self.playlistOperator.printPlaylist()


    def removeSongWithUser(self):
        self.playlistOperator.removeSongWithUser()


    def play(self):
        print("\nPlaying...")
        self.printPlaylist()

