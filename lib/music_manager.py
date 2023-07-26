class MusicManager():

    def __init__(self):
        self.music_history = []

    def list_music(self):
        return self.music_history

    def add(self, song):
        self.music_history.append(song)