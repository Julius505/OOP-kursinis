import sys
import os

# Add the project root directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from src.models.timetable import Timetable
from src.models.movie import RegularMovie, IMAXMovie

class TestTimetable(unittest.TestCase):
    def setUp(self):
        self.timetable = Timetable.get_instance()
        self.movie1 = RegularMovie("The Shawshank Redemption", 142)
        self.movie2 = IMAXMovie("Dune: Part Two", 166)
        self.timetable.movie_library.add_movie(self.movie1)
        self.timetable.movie_library.add_movie(self.movie2)

    def test_add_screening(self):
        self.timetable.add_screening("The Shawshank Redemption", "10:00")
        self.assertEqual(len(self.timetable.screenings), 1)

    def test_remove_screening(self):
        self.timetable.add_screening("The Shawshank Redemption", "10:00")
        self.timetable.remove_screening("10:00")
        self.assertEqual(len(self.timetable.screenings), 0)

    def test_change_movie(self):
        self.timetable.add_screening("The Shawshank Redemption", "10:00")
        self.timetable.change_movie("10:00", "Dune: Part Two")
        screening = self.timetable.screenings[0]
        self.assertEqual(screening.get_movie().title, "Dune: Part Two")

    def test_display_timetable(self):
        self.timetable.add_screening("The Shawshank Redemption", "10:00")
        self.timetable.add_screening("Dune: Part Two", "13:30")
        self.assertEqual(len(self.timetable.screenings), 2)

if __name__ == "__main__":
    unittest.main()