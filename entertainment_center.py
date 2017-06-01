"""Lists all details of movies and displays them on a website."""
import fresh_tomatoes
import media

def entertainment():
    """Creates Movies objects with title, storyline, poster image link, video trailer link."""
    bahubali = media.Movie("Bahubali",
                          "The film about Shiva, the son of Bahubali, begins to search for answers after he learns about his heritage.",
                          "http://www.impawards.com/intl/india/2015/posters/bahubali_the_beginning_ver2.jpg",
                          "https://www.youtube.com/watch?v=sOEg_YZQsTI"
                          )

    pk 		= media.Movie("PK",
                          "PK the alien who encounters the other side of God and religion on earth, in India.",
                          "http://www.impawards.com/intl/india/2014/posters/pk.jpg",
                          "https://www.youtube.com/watch?v=SOXWc32k4zA"
                          )

    the_mummy = media.Movie("The Mummy",
                           "The Mummy is a rousing, suspenseful and horrifying epic about an expedition of treasure-seeking.",
                           "http://www.impawards.com/2017/posters/mummy_ver3.jpg",
                           "https://www.youtube.com/watch?v=GzorZUuZqEI"
                           )

    alien = media.Movie("Alien: Covenant",
                         "A film about bound for a remote planet on the far side of the galaxy.",
                         "http://www.impawards.com/2017/posters/alien_covenant_ver5_xlg.jpg",
                         "https://www.youtube.com/watch?v=svnAD0TApb8"
                         )

    king_arthur = media.Movie("King Arthur",
                           "A film about mythological figure who was the head of the kingdom Camelot",
                           "http://www.impawards.com/2017/posters/king_arthur_legend_of_the_sword.jpg",
                           "https://www.youtube.com/watch?v=ja9kDkmjdHQ"
                           )

    transformers = media.Movie("Transformers",
                          "The fate of humanity is at stake when two races of robots, the good Autobots"
                          "and the villainous Decepticons, bring their war to Earth.",
                          "http://www.impawards.com/2017/posters/transformers_the_last_knight_ver2.jpg",
                          "https://www.youtube.com/watch?v=sgnO5fO46pE"
                          )

    # Store objects of Movie in a list.
    movies = [bahubali, pk, the_mummy, alien, king_arthur, transformers]

    # Open the movie website in the user's browser.
    fresh_tomatoes.open_movies_page(movies)

#method invoke.
entertainment()
