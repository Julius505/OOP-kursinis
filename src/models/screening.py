class Screening:
    def __init__(self, movie, time):
        self.__movie = movie
        self.time = time

    def get_movie(self):
        return self.__movie

    def __str__(self):
        return f"{self.time} - {self.__movie}"