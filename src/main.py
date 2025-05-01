import sys
import os

# Add the project root directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.models.timetable import Timetable
from src.models.movie import RegularMovie, IMAXMovie

# Dynamically construct the absolute path to the 'data' folder
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_dir = os.path.join(project_root, "data")

# Ensure the 'data' directory exists
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

print("=== MOVIE THEATRE MANAGEMENT SYSTEM ===")

timetable = Timetable.get_instance()

library = timetable.movie_library
library.add_movie(RegularMovie("The Shawshank Redemption", 142))
library.add_movie(IMAXMovie("Dune: Part Two", 166))
library.add_movie(RegularMovie("The Godfather", 175))
library.add_movie(IMAXMovie("Interstellar", 169))
library.add_movie(RegularMovie("Inception", 148))
library.add_movie(IMAXMovie("Avatar: The Way of Water", 192))
library.add_movie(RegularMovie("Pulp Fiction", 154))
library.add_movie(IMAXMovie("The Dark Knight", 152))
library.add_movie(RegularMovie("Forrest Gump", 142))
library.add_movie(IMAXMovie("Avengers: Endgame", 181))

# Save and load movie library
movies_file = os.path.join(data_dir, "movies.txt")
library.save_to_file(movies_file)
library.load_from_file(movies_file)

library.show_movies()

# Save and load timetable
timetable_file = os.path.join(data_dir, "timetable.txt")
timetable.add_screening("Avatar: The Way of Water", "12:00")
timetable.add_screening("The Dark Knight", "18:00")
timetable.add_screening("Forrest Gump", "21:00")
timetable.add_screening("The Shawshank Redemption", "10:00")
timetable.add_screening("Dune: Part Two", "13:30")
timetable.save_to_file(timetable_file)
timetable.load_from_file(timetable_file)

timetable.display_timetable()

timetable.change_movie("16:15", "Interstellar")
timetable.add_screening("Doogal", "07:55")
timetable.change_movie("00:00", "Interstellar")
timetable.remove_screening("13:30")

timetable.display_timetable()

timetable.remove_screening("13:30")