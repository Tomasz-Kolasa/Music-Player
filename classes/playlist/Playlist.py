from .PlaylistItem import PlaylistItem

class Playlist:
    def __init__(self):
        self.playlistItems = []
        

    def addItem(self, item:PlaylistItem):
        self.playlistItems.append(item)


    def removeItem(self, index:int):
        del self.playlistItems[index]