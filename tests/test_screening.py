import sys
import os

# Add the project root directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from src.models.movie import RegularMovie
from src.models.screening import Screening

class TestScreening(unittest.TestCase):
    def setUp(self):
        self.movie = RegularMovie("The Shawshank Redemption", 142)
        self.screening = Screening(self.movie, "10:00")

    def test_get_movie(self):
        self.assertEqual(self.screening.get_movie().title, "The Shawshank Redemption")

    def test_screening_time(self):
        self.assertEqual(self.screening.time, "10:00")

    def test_screening_str(self):
        self.assertEqual(str(self.screening), "10:00 - The Shawshank Redemption (142 min) [Regular]")

if __name__ == "__main__":
    unittest.main()