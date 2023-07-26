class GrammarStats:
    def __init__(self):
        self.check_history = {
            'True': 0,
            'False': 0
        }

    def check(self, text):
        cap = text[:1]
        dot = text[-1:]
        if cap == cap.upper() and dot == '.':
            self.check_history['True'] += 1 
            return True
        else:
            self.check_history['False'] += 1 
            return False

    def percentage_good(self):
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        total = self.check_history['True'] + self.check_history['False']
        
        return (self.check_history['True'] / total) * 100