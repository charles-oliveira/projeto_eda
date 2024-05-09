from CircularLinkedList import CircularLinkedList
from DoublyLinkedList import DoublyLinkedList

class MusicManagement:
    def __init__(self):
        self.playlist = CircularLinkedList()
        self.history = DoublyLinkedList()

    def add_song_to_playlist(self, song):
        self.playlist.insert_end(song)

    def remove_song_from_playlist(self, song):
        self.playlist.remove(song)

    def add_song_to_history(self, song):
        self.history.insert_end(song)

    def remove_song_from_history(self, song):
        self.history.remove(song)

    def search_playlist(self, song):
        return self.playlist.search(song)

    def search_history(self, song):
        return self.history.search(song)

    def play_next_song(self):
        song = self.playlist.head.data
        self.playlist.head = self.playlist.head.next
        self.add_song_to_history(song)
        return song

    def play_previous_song(self):
        song = self.history.head.data
        self.history.head = self.history.head.prev
        self.add_song_to_playlist(song)
        return song
    

def tester():
    music_manager = MusicManagement()
    music_manager.add_song_to_playlist("Song1")
    music_manager.add_song_to_playlist("Song2")
    music_manager.add_song_to_playlist("Song3")
    music_manager.add_song_to_playlist("Song4")
    music_manager.add_song_to_playlist("Song5")

    print("Playlist:")
    current = music_manager.playlist.head
    count = 0
    while current:
        print(current.data)
        current = current.next
        count += 1
        if count == 6:  # Adicionado para evitar loop infinito
            break

    print("History:")
    current = music_manager.history.head
    count = 0
    while current:
        print(current.data)
        current = current.next
        count += 1
        if count == 6:  # Adicionado para evitar loop infinito
            break
    
    print("Playing next song")
    print(music_manager.play_next_song())
    print("Playlist:")
    current = music_manager.playlist.head
    count = 0
    while current:
        print(current.data)
        current = current.next
        count += 1
        if count == 6:  # Adicionado para evitar loop infinito
            break
    
    print("Back to previous song")
    print(music_manager.play_previous_song())
    print("Playlist:")
    current = music_manager.playlist.head
    count = 0
    while current:
        print(current.data)
        current = current.next
        count += 1
        if count == 6:  # Adicionado para evitar loop infinito
            break

if __name__ == "__main__":
    tester()
