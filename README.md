# Kino teatro tvarkaraščio tvarkymo sistema

## 1. Introduction

### Kas tai?

Tai yra Python pagrindu sukurta programa, skirta koreguoti simuliuojamą kino teatro tvarkaraštį.

### Kaip įjungti šią programą?

Būtina turėti įdiegtą Python programą, kurios versija yra 3.8 ar naujesnė. Tada reikia klonuoti saugyklą (angl. repository), nurodyti projekto vietą ir įsitikinkiti, kad duomenų katalogas egzistuoja:
```bash
git clone https://github.com/your-username/movie-theatre-management.git
cd movie-theatre-management
mkdir data
```
Tada galite paleisti programą:
```
python src/main.py
```

### Kaip ją naudoti?

Kai paleisite programą, ji jums parodys filmų bibliotekoje esančius filmus ir dabartinį filmų tvarkaraštį.
Jūs galite:
* Pridėti naujų filmų į filmų biblioteką.
* Pridėti naują filmą į tvarkaraštį laisvai parinktu laiku.
* Pašalinti ar pakeisti esamą filmą tvarkaraštyje.
* Rodyti filmų bibliotekoje esančius filmus arba dabartinį filmų tvarkaraštį.

## 2. Pagrindo analizė

Stengiausi kuo arčiau sekti PEP8 stiliaus nurodymus Python kalbos programai.

### Objektinio programavimo pagrindų implementacija
#### Paveldėjimas (angl. Inheritance) ir Abstrakcija (angl. Abstraction):
* Paveldėjimas yra objektinio programavimo principas, kuris leidžia vienai klasei (dukterinei klasei) perimti kitos klasės (tėvinės klasės) savybes ir metodus. Tai reiškia, kad dukterinė klasė gali naudoti tėvinės klasės funkcionalumą, o prireikus – jį praplėsti ar pakeisti.

* Abstrakcija yra objektinio programavimo principas, kuris leidžia paslėpti sudėtingas detales ir pateikti tik svarbiausią informaciją. Tai reiškia, kad abstrakcija leidžia sukurti bendrą sąsają (angl. interface), kurią gali naudoti įvairios klasės, nepriklausomai nuo jų vidinės implementacijos.

Mano programoje abu šie principai yra panaudoti norint praplėsti filmų įvairovę:
```
class Movie(ABC):
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    @abstractmethod
    def get_type(self):  # Abstraktus metodas, kurį implementuoja dukterinės klasės.
        pass

    def __str__(self):  # Šis metodas grąžina žmogui suprantamą objekto reprezentaciją.
        return f"{self.title} ({self.duration} min) [{self.get_type()}]"


class RegularMovie(Movie):  # Paveldėjimas: Dukterinė klasė "RegularMovie" yra tėvinės klasės "Movie" specifinis atvėjis.
    def get_type(self):  # Abstraktaus metodo implementacija
        return "Regular"


class IMAXMovie(Movie):  # Paveldėjimas: Dukterinė klasė "IMAXMovie" yra tėvinės klasės "Movie" specifinis atvėjis.
    def get_type(self):  # Abstraktaus metodo implementacija
        return "IMAX"
```

#### Polimorfizmas (angl. Polymorphism):
* Polimorfizmas yra objektinio programavimo principas, kuris leidžia vienodai naudoti skirtingų klasių objektus, jei jie turi bendrą sąsają (metodą tuo pačiu pavadinimu). Kitaip tariant, polimorfizmas leidžia naudoti tą patį metodą skirtingiems objektams, o kiekvienas objektas elgiasi pagal savo implementaciją.

Anksčiau parodytoje kodo iškarpoje tuo pačiu, nors ir neakivaizdžiai, veikia ir polimorfizmas su abstrakčiu metodu "get_type". Šis metodas yra iškviečiamas norint atvaizduoti filmus esančius filmų bibliotekoje ir filmus esančius tvarkaraštyje, jis nurodo filmo tipą (Regular arba IMAX):
```
Available Movies:  # Filmų bibliotekos vaizdavimas
------------------
The Shawshank Redemption (142 min) [Regular]
Dune: Part Two (166 min) [IMAX]
The Godfather (175 min) [Regular]
Interstellar (169 min) [IMAX]
Inception (148 min) [Regular]
Avatar: The Way of Water (192 min) [IMAX]
Pulp Fiction (154 min) [Regular]
The Dark Knight (152 min) [IMAX]
Forrest Gump (142 min) [Regular]
Avengers: Endgame (181 min) [IMAX]
------------------
Current Timetable:  # Tvarkaraščio vaizdavimas
------------------
10:00 - The Shawshank Redemption (142 min) [Regular]
12:00 - Avatar: The Way of Water (192 min) [IMAX]
13:30 - Dune: Part Two (166 min) [IMAX]
18:00 - The Dark Knight (152 min) [IMAX]
21:00 - Forrest Gump (142 min) [Regular]
------------------
```

#### Enkapsuliacija (angl. Encapsulation):
* Enkapsuliacija yra objektinio programavimo principas, kuris leidžia paslėpti objekto vidinę būseną (duomenis) ir suteikti prieigą prie jų tik per viešus metodus. Tai padeda apsaugoti duomenis nuo netinkamo naudojimo ir leidžia kontroliuoti, kaip jie yra keičiami.

```
class Screening:
    def __init__(self, movie, time):
        self.__movie = movie  # Atributas "movie" enkapsuliuojamas į privatų atributą.
        self.time = time

    def get_movie(self):  # Viešas metodas, leidžiantis pasiekti privataus atributo informaciją apie filmą.
        return self.__movie

    def __str__(self):
        return f"{self.time} - {self.__movie}"
```

#### Dizaino modelis:
Savo programoje panaudojau Singleton dizaino modelį, kuris užtikrina, kad tam tikros klasės objektas būtų sukurtas tik vieną kartą per visą programos veikimo laiką. Tai reiškia, kad visos programos dalys naudos tą patį objekto atvėjį (angl. instance).

Naudoju būtent šį dizaino modelį, nes noriu užtikrinti, kad visi mano kino teatro darbuotojai turėtų prieigą prie vieno ir to pačio tvarkaraščio.
```
class Timetable:
    __instance = None  # Privatus klasės atributas, skirtas saugoti vienintelį klasės atvėjį.

    @staticmethod
    def get_instance():
        if Timetable.__instance is None:  # Patikrinama, ar dar neegzistuoja klasės atvėjis.
            Timetable()  # Jei atvėjis neegzistuoja, jis sukuriamas.
        return Timetable.__instance  # Jei atvėjis jau egzistuoja, grąžinamas tas pats atvėjis.

    def __init__(self):  # Konstruktorius užtikrina, kad naujas egzempliorius negali būti sukurtas tiesiogiai naudojant Timetable().
        if Timetable.__instance is not None:
            raise Exception("Timetable yra Singleton! Naudokite get_instance() metodą.")
        else:
            Timetable.__instance = self
            self.screenings = []
            self.movie_library = MovieLibrary()
```

#### Kompozicija (angl. Composition) ir Agregacija (angl. Aggregation):
Kompozicija yra objektinio programavimo principas, kuris leidžia vieną klasę sudaryti iš kitų klasių objektų. Kitaip tariant, kompozicija reiškia, kad klasė „turi“ kitų klasių objektus kaip savo dalis. Tai leidžia kurti sudėtingesnes sistemas, sudedant jas iš mažesnių, nepriklausomų komponentų. Jei pagrindinė klasė sunaikinama, sunaikinami ir jos komponentai.

Agregacija yra objektinio programavimo principas, kuris apibūdina „turi“ santykį tarp klasių, tačiau su silpnesniu ryšiu nei kompozicija. Agregacijoje viena klasė naudoja kitos klasės objektą kaip savo dalį, tačiau tas objektas gali egzistuoti nepriklausomai nuo pagrindinės klasės. Jei pagrindinė klasė sunaikinama, susieti objektai išlieka.
```
class Timetable:
    def __init__(self):
        if Timetable.__instance is not None:
            print("Error: Timetable is a singleton! Use get_instance() instead.")
        else:
            Timetable.__instance = self
            self.screenings = []  # Agregacija: klasė "Timetable" turi rodinių (angl. screening) sąrašą.
            self.movie_library = MovieLibrary()  # Kompozicija: klasė "Timetable" turi klasės "MovieLibrary" objektą.

    def add_screening(self, movie_title, time):
        for screening in self.screenings:
            if screening.time == time:
                print(f"Error: A screening already exists at {time}.")
                return

        movie = self.movie_library.get_movie(movie_title)
        if movie:
            screening = Screening(movie, time)
            self.screenings.append(screening)  # Agregacija: į tą sąrašą įdedama klasės Screening objekto informacija.
            print(f"Added screening: {screening}")
        else:
            print(f"Error: Movie '{movie_title}' not found in the library.")
```

#### Įrašymas į failą ir skaitymas iš failo:
Įrašymas į failą ir skaitymas iš failo leidžia išsaugoti programos duomenis (filmų biblioteką arba tvarkaraštį) į tekstinius failus ir vėliau juos atkurti. Tai užtikrina, kad duomenys išliks net ir uždarius programą.
```
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
```

#### Kodo testavimas:
Savo kodo testus atlikau panaudodamas unittest komandą. Testai parodo, ar programos dalys veikia tinkamai.
##### Mano programos testai ir jų rezultatai:
* Klasės MovieLibrary:
```
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
```
```
Added movie to library: The Shawshank Redemption (142 min) [Regular]
.Added movie to library: Dune: Part Two (166 min) [IMAX]
.Added movie to library: The Shawshank Redemption (142 min) [Regular]
Added movie to library: Dune: Part Two (166 min) [IMAX]
.
----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
```
* Klasės Screening:
```
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
```
```
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
```
* Klasės Timetable:
```
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
```
```
Added movie to library: The Shawshank Redemption (142 min) [Regular]
Added movie to library: Dune: Part Two (166 min) [IMAX]
Added screening: 10:00 - The Shawshank Redemption (142 min) [Regular]
.Added movie to library: The Shawshank Redemption (142 min) [Regular]
Added movie to library: Dune: Part Two (166 min) [IMAX]
Error: A screening already exists at 10:00.
Changed movie at 10:00 to Dune: Part Two (166 min) [IMAX]
.Added movie to library: The Shawshank Redemption (142 min) [Regular]
Added movie to library: Dune: Part Two (166 min) [IMAX]
Error: A screening already exists at 10:00.
Added screening: 13:30 - Dune: Part Two (166 min) [IMAX]
.Added movie to library: The Shawshank Redemption (142 min) [Regular]
Added movie to library: Dune: Part Two (166 min) [IMAX]
Error: A screening already exists at 10:00.
Removed screening at 10:00
F
======================================================================
FAIL: test_remove_screening (__main__.TestTimetable.test_remove_screening)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "c:\Users\EpicGamerPC\Desktop\studijos\Semestras_2\Objektinis programavimas\Kursinisd\movie_theatre_management\tests\test_timetable.py", line 26, in test_remove_screening
    self.assertEqual(len(self.timetable.screenings), 0)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 1 != 0

----------------------------------------------------------------------
Ran 4 tests in 0.002s

FAILED (failures=1)
```

## 3. Rezultatai ir Išvados:
* Sukūriau primityvią kino teatro tvarkaraščio valdymo sistemą.
* Sėkmingai pritaikiau objektinio programavimo principus.
* Sukurti programos testai parodė, jog mano pagrindinės programos klasės yra pakankamai patikimos, tačiau gali būti patobulintos.
* Su sunkiausiais iššūkiais susidūriau transformuojant parašytą kodą į katalogą ir dirbant su GitHub.

### Tobulinimo galimybės:
* Ši primityvi programa gali būti naudojama kaip pagrindas realiai kino teatro valdymo sistemai.
* Nepraeitas paskutinis testas rodo, kad reikėtų pakoreguoti Timetable klasę.
