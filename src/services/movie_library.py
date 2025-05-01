from src.models.movie import RegularMovie, IMAXMovie


class MovieLibrary:
    def __init__(self):
        self.movies = {}

    def add_movie(self, movie):
        self.movies[movie.title] = movie
        print(f"Added movie to library: {movie}")

    def get_movie(self, title):
        return self.movies.get(title)

    def show_movies(self):
        print("\nAvailable Movies:")
        print("------------------")
        for movie in self.movies.values():
            print(movie)
        print("------------------")

    def save_to_file(self, filename):
        with open(filename, "w") as file:
            for movie in self.movies.values():
                file.write(f"{movie.title},{movie.duration},{movie.get_type()}\n")
        print(f"Movie library saved to {filename}")

    def load_from_file(self, filename):
        try:
            with open(filename, "r") as file:
                for line in file:
                    title, duration, movie_type = line.strip().split(",")
                    duration = int(duration)
                    if movie_type == "Regular":
                        self.add_movie(RegularMovie(title, duration))
                    elif movie_type == "IMAX":
                        self.add_movie(IMAXMovie(title, duration))
            print(f"Movie library loaded from {filename}")
        except FileNotFoundError:
            print(f"Error: File {filename} not found.")