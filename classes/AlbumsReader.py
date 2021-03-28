from .Song import Song

class AlbumsReader:
    def __init__(self, albums:list):
        self.albums = albums


    def isSongExists(self, albumNumber, songNumber):
        if( albumNumber in range(1, len(self.albums)+1) ):
            albumSongs = self.albums[albumNumber-1][3]
            if(songNumber in range(1, len(albumSongs)+1)):
                return True
        return False


    def printAlbums(self):
        for index, (albumTitle, artist, year, songs) in enumerate(self.albums):
            print("{}: {}, {}, {}".format(index + 1, albumTitle, artist, year))
            for song in songs:
                print("   {0}. {1}".format(song[0],song[1]))


    def getSongByAlbumNoAndSongNo(self, albumNumber, songNumber)->Song:
        if(not self.isSongExists(albumNumber, songNumber)):
            raise Exception(f"Song {albumNumber},{songNumber} doesn't exists.")
        for index, (albumTitle, artist, year, songs) in enumerate(self.albums):
            for songTuple in songs:
                if index+1==albumNumber and songTuple[0]==songNumber:
                    song = Song(songTuple[1])
                    song.album = albumTitle
                    song.artist = artist
                    song.year = year
                    song.no = songTuple[0]
                    return song
