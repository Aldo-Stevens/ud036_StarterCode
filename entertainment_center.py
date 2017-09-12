import fresh_tomatoes
import media

transformers = media.Movie(
    "Transformers",
    "Storyline",
    "https://upload.wikimedia.org/wikipedia/en/9/94/Transformers_Age_of_Extinction_Poster.jpeg", # NOQA
    "https://www.youtube.com/watch?v=HKi0xnV4ZjM")

thor = media.Movie(
    "Thor Ragnarok",
    "Storyline",
    "https://i.pinimg.com/736x/ee/0f/3d/ee0f3de4a131a6e4a3402a3d8135ba94--marvel-movies-thor.jpg", # NOQA
    "https://www.youtube.com/watch?v=4yqM06buDsk")

george_of_the_jungle = media.Movie(
    "George of the Jungle",
    "Storyline",
    "https://vignette2.wikia.nocookie.net/disney/images/f/f8/George_Of_The_Jungle.jpg/revision/latest?cb=20140328163833", # NOQA
    "https://www.youtube.com/watch?v=PP9VGoP8xnI")

the_mummy = media.Movie(
    "The Mummy",
    "Storyline",
    "http://vignette1.wikia.nocookie.net/universalstudios/images/2/2e/The_Mummy_%282017%29_teaser_poster.jpg/revision/latest?cb=20161208002812", # NOQA
    "https://www.youtube.com/watch?v=sCdV3esMr9M")

petes_dragon = media.Movie(
    "Pete's Dragon",
    "Storyline",
    "http://vignette4.wikia.nocookie.net/disney/images/1/1e/Pete%27s_Dragon_%282016%29_Soundtrack.jpg/revision/latest?cb=20160721171139", # NOQA
    "https://www.youtube.com/watch?v=fPOamb6d_20")

hunger_games = media.Movie(
    "Hunger Games",
    "Storyline",
    "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg", # NOQA
    "https://www.youtube.com/watch?v=PbA63a7H0bo")

movie_300 = media.Movie(
    "300",
    "300 spartans vs an amry of persians",
    "https://upload.wikimedia.org/wikipedia/en/5/5c/300poster.jpg", # NOQA
    "https://www.youtube.com/watch?v=wDiUG52ZyHQ")

movies = [transformers, movie_300, george_of_the_jungle, 
          thor, the_mummy, petes_dragon, hunger_games]

fresh_tomatoes.open_movies_page(movies)
