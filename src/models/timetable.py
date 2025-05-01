from src.models.screening import Screening
from src.services.movie_library import MovieLibrary


class Timetable:
    __instance = None

    @staticmethod
    def get_instance():
        if Timetable.__instance is None:
            Timetable()
        return Timetable.__instance

    def __init__(self):
        if Timetable.__instance is not None:
            print("Error: Timetable is a singleton! Use get_instance() instead.")
        else:
            Timetable.__instance = self
            self.screenings = []
            self.movie_library = MovieLibrary()

    def add_screening(self, movie_title, time):
        for screening in self.screenings:
            if screening.time == time:
                print(f"Error: A screening already exists at {time}.")
                return

        movie = self.movie_library.get_movie(movie_title)
        if movie:
            screening = Screening(movie, time)
            self.screenings.append(screening)
            print(f"Added screening: {screening}")
        else:
            print(f"Error: Movie '{movie_title}' not found in the library.")

    def remove_screening(self, time):
        for screening in self.screenings:
            if screening.time == time:
                self.screenings.remove(screening)
                print(f"Removed screening at {time}")
                return
        print(f"Error: No screening found at {time}")

    def change_movie(self, time, new_movie_title):
        new_movie = self.movie_library.get_movie(new_movie_title)
        if not new_movie:
            print(f"Error: Movie '{new_movie_title}' not found in library.")
            return
        for screening in self.screenings:
            if screening.time == time:
                screening._Screening__movie = new_movie
                print(f"Changed movie at {time} to {new_movie}")
                return
        print(f"Error: No screening found at {time}")

    def display_timetable(self):
        if not self.screenings:
            print("Timetable is empty.")
            return
        print("\nCurrent Timetable:")
        print("------------------")
        for screening in sorted(self.screenings, key=lambda x: x.time):
            print(screening)
        print("------------------")

    def save_to_file(self, filename):
        with open(filename, "w") as file:
            for screening in self.screenings:
                movie = screening.get_movie()
                file.write(f"{screening.time},{movie.title}\n")
        print(f"Timetable saved to {filename}")

    def load_from_file(self, filename):
        try:
            with open(filename, "r") as file:
                for line in file:
                    time, movie_title = line.strip().split(",")
                    self.add_screening(movie_title, time)
            print(f"Timetable loaded from {filename}")
        except FileNotFoundError:
            print(f"Error: File {filename} not found.")