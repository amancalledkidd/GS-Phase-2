class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        self.chunks = []

    def format(self):
        return f"{self.title}: {self.contents}"

    def count_words(self):
        string = (self.contents).split(" ")
        return len(string)

    def reading_time(self, wpm):
        import math

        word_count = self.count_words()
        return math.ceil(word_count / int(wpm))

    def reading_chunk(self, wpm, minutes):
        
        words_to_read = wpm * minutes
        string = (self.contents).split(" ")
        if self.chunks != []:
            slice = (" ").join(self.chunks[:words_to_read])
            self.chunks = self.chunks[words_to_read:]
        else:
            slice = (" ").join(string[:words_to_read])
            self.chunks = string[words_to_read:]
        
        return slice
        
