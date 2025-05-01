import sys
import os

# Add the project root directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from src.models.movie import RegularMovie, IMAXMovie
from src.services.movie_library import MovieLibrary

class TestMovieLibrary(unittest.TestCase):
    def setUp(self):
        self.library = MovieLibrary()
        self.movie1 = RegularMovie("The Shawshank Redemption", 142)
        self.movie2 = IMAXMovie("Dune: Part Two", 166)

    def test_add_movie(self):
        self.library.add_movie(self.movie1)
        self.assertIn("The Shawshank Redemption", self.library.movies)

    def test_get_movie(self):
        self.library.add_movie(self.movie2)
        movie = self.library.get_movie("Dune: Part Two")
        self.assertEqual(movie.title, "Dune: Part Two")
        self.assertEqual(movie.duration, 166)

    def test_show_movies(self):
        self.library.add_movie(self.movie1)
        self.library.add_movie(self.movie2)
        self.assertEqual(len(self.library.movies), 2)

if __name__ == "__main__":
    unittest.main()