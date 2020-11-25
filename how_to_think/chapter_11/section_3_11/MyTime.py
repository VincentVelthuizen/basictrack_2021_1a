def add_time(t1, t2):
    secs = t1.to_seconds() + t2.to_seconds()
    return MyTime(0, 0, secs)


class MyTime:

    def __init__(self, hrs=0, mins=0, secs=0):
        total_seconds = hrs * 3600 + mins * 60 + secs

        self.hours = total_seconds // 3600
        self.minutes = (total_seconds % 3600) // 60
        self.seconds = total_seconds % 60

    def to_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def after(self, time2):
        return self.to_seconds() > time2.to_seconds()

    def between(self, t1, t2):
        return self.after(t1) and t2.after(self)

    def increment(self, seconds):
        total_seconds = self.to_seconds() + seconds

        self.hours = total_seconds // 3600
        self.minutes = (total_seconds % 3600) // 60
        self.seconds = total_seconds % 60

        return self

    def __add__(self, other):
        return MyTime(0, 0, self.to_seconds() + other.to_seconds())

    def __gt__(self, other):
        return self.after(other)

    def __str__(self):
        return "{:0>2d}:{:0>2d}:{:0>2d}".format(self.hours, self.minutes, self.seconds)
