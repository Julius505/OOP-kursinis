from abc import ABC, abstractmethod


class Movie(ABC):
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    @abstractmethod
    def get_type(self):
        pass

    def __str__(self):
        return f"{self.title} ({self.duration} min) [{self.get_type()}]"


class RegularMovie(Movie):
    def get_type(self):
        return "Regular"


class IMAXMovie(Movie):
    def get_type(self):
        return "IMAX"