

class Diary:
    def __init__(self):
        self.entry_list = []

    def add(self, entry):
        self.entry_list.append(entry)

    def all(self):
        return self.entry_list

    def count_words(self):
        total = 0
        for entry in self.entry_list:
            total += entry.count_words()
        return total

    def reading_time(self, wpm):
        total = 0
        for entry in self.entry_list:
            total += entry.reading_time(wpm)
        return total

    def find_best_entry_for_reading_time(self, wpm, minutes):
        import math
        read_size = wpm * minutes
        best_option_num = 0
        for entry in self.entry_list:
            if entry.count_words() < read_size:
                if entry.count_words() > best_option_num:
                    best_option = entry
                    best_option_num = entry.count_words()
        return best_option
