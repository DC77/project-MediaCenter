__author__ = 'daveCiampa'

import media
import fresh_tomatoes

rush = media.Movie("Rush", "History of two of the best F1 drivers",
                        "https://upload.wikimedia.org/wikipedia/en/d/d0/Rush_UK_poster.jpeg",
                        "https://www.youtube.com/watch?v=L_u3FODrenM")

pacific_rim = media.Movie("Pacific Rim", "Aliens vs. Mechs",
                        "https://upload.wikimedia.org/wikipedia/en/f/f3/Pacific_Rim_FilmPoster.jpeg",
                        "https://www.youtube.com/watch?v=5guMumPFBag")

love_actually = media.Movie("Love Actually", "If you look for it, I've got a sneaky feeling you'll find that love actually is all around.",
                        "https://upload.wikimedia.org/wikipedia/en/e/eb/Love_Actually_movie.jpg",
                        "https://www.youtube.com/watch?v=_eCb8w8SRAk")

interstellar = media.Movie("Interstellar", "The world is dieing, humaity has to find a new home.",
                        "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
                        "https://www.youtube.com/watch?v=0vxOhd4qlnA")

elf = media.Movie("Elf", "A confused Elf explores New York.",
                        "https://upload.wikimedia.org/wikipedia/en/d/df/Elf_movie.jpg",
                        "https://www.youtube.com/watch?v=_TOQWF_-RWY")

guardians = media.Movie("Guardians of the Galaxy", "Band of misfits saves the galaxy.",
                        "https://upload.wikimedia.org/wikipedia/en/8/8f/GOTG-poster.jpg",
                        "https://www.youtube.com/watch?v=B16Bo47KS2g")

movies = [rush, pacific_rim, love_actually, interstellar, elf, guardians]
fresh_tomatoes.open_movies_page(movies)


