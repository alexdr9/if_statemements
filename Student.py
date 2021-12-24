# ----------- day 11

class Student:
    def __init__(self, name, subject, score):
        self.name = name
        self.subject = subject
        self.score = score

    def on_honour_roll(self):
        if self.score >= 2.1:
            return True
        else:
            return False


