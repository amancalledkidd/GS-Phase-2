# File: lib/vowel_remover.py

class VowelRemover:
    def __init__(self, text):
        self.text = text
        self.vowels = ["a", "e", "i", "o", "u"]

    def remove_vowels(self):
        for i in self.text:
            if i.lower() in self.vowels:
                self.text = self.text.replace(i, "")
        return self.text

