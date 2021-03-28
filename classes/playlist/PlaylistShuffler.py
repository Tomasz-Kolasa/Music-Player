from .Playlist import Playlist
import random, math

class PlaylistShuffler:
    def __init__(self, playlist:Playlist):
        self.playlist = playlist
        self.shuffleHistory = []

    def shuffle(self):
        setsQty = len( self.shuffleHistory )
        itemsQty = len( self.playlist.playlistItems )
        if(0==setsQty):
            raise Exception("\nPlaylist empty!")
        if(1==len(self.playlist.playlistItems)):
            raise Exception("\nCan't shuffle one item!")

        if( math.factorial(itemsQty) == setsQty):
            self.resetShuffleHistory()
            raise Exception("\nThe maximum number of shuffle combinations reached! Order reseted.")

        self.addRandomSet()
        

    def addRandomSet(self):
        newSet = self.shuffleHistory[0].copy()
        while(True):
            random.shuffle(newSet)
            if self.isUnique(newSet):
                self.shuffleHistory.append(newSet)
                break


    def isUnique(self, newSet):
        for set in self.shuffleHistory:
            if set == newSet:
                return False
        return True


    def resetShuffleHistory(self):
        self.shuffleHistory = []
        playlistItemsQty = len( self.playlist.playlistItems )
        if playlistItemsQty>0:
            shuffleSet = []
            for i in range(playlistItemsQty):
                shuffleSet.append(i)
            self.shuffleHistory.append(shuffleSet)