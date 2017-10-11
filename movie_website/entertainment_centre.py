import fresh_tomatoes
import media

the_italian_job = media.Movie("The Italian Job ", "After being betrayed and left for dead in Italy, Charlie Croker and his team plan an elaborate gold heist against their former ally.",
                              "https://upload.wikimedia.org/wikipedia/en/d/db/Italianjob.jpg",
                              "https://www.youtube.com/watch?v=5Eyw-Qiwpj0", "2003","110 Minutes","English","(7.0/10)")

the_transporter = media.Movie("The Transporter", "Frank is hired to transport packages for unknown clients and has made a very good living doing so. But when asked to move a package that begins moving, complications arise.",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/6/68/Transporterposter.jpg/220px-Transporterposter.jpg",
                        "https://www.youtube.com/watch?v=0poXFSvX0_4", "2002","92 Minutes","English","(6.8/10)")

the_avengers = media.Movie("The Avengers", "Earth's mightiest heroes must come together and learn to fight as a team if they are to stop the mischievous Loki and his alien army from enslaving humanity.",
                     "https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg",
                     "https://www.youtube.com/watch?v=eOrNdBpGMv8", "2012", "143 Minutes", "English","(8.1/10)" )


the_hobbit = media.Movie("The Hobbit: An Unexpected Journey", "A reluctant hobbit, Bilbo Baggins, sets out to the Lonely Mountain with a spirited group of dwarves to reclaim their mountain home, and the gold within it from the dragon Smaug.",
                          "https://upload.wikimedia.org/wikipedia/en/b/b3/The_Hobbit-_An_Unexpected_Journey.jpeg",
                          "https://www.youtube.com/watch?v=SDnYMbYB-nU",  "2012", "169 Minutes", "English","(8.1/10)" )

the_chronicles_of_narnia = media.Movie("The Chronicles of Narnia: The Lion, The Witch and The Wardrobe", "Four kids travel through a wardrobe to the land of Narnia and learn of their destiny to free it with the guidance of a mystical lion.",
                                "https://upload.wikimedia.org/wikipedia/en/1/10/The_Chronicles_of_Narnia_-_The_Lion%2C_the_Witch_and_the_Wardrobe.jpg",
                                "https://www.youtube.com/watch?v=lWKj41HZBzM", "2005", "145 Minutes", "English","(6.9/10)" )

madagascar = media.Movie("Madagascar:Escape to Africa", "The animals try to fly back to New York City, but crash-land on an African wildlife refuge, where Alex is reunited with his parents.",
                             "https://upload.wikimedia.org/wikipedia/en/7/7f/Madagascar2poster.jpg",
                             "https://www.youtube.com/watch?v=A45jv8uhZwo",  "2008", "89 Minutes", "English","(6.7/10)" )

taare_zameen_par = media.Movie("Taare Zameen Par", "An eight-year-old boy is thought to be a lazy trouble-maker, until the new art teacher has the patience and compassion to discover the real problem behind his struggles in school.",
                             "https://upload.wikimedia.org/wikipedia/en/b/b4/Taare_Zameen_Par_Like_Stars_on_Earth_poster.png",
                             "https://www.youtube.com/watch?v=Mcs1O4_7iTc",  "2007", "164 Minutes", "Hindi","(8.5/10)" )

three_idiots = media.Movie("3:Idiots", "Two friends are searching for their long lost companion. They revisit their college days and recall the memories of their friend who inspired them to think differently, even as the rest of the world called them idiots.",
                             "https://upload.wikimedia.org/wikipedia/en/d/df/3_idiots_poster.jpg",
                             "https://www.youtube.com/watch?v=K0eDlFX9GMc",  "2009", "171 Minutes", "Hindi","(8.4/10)" )

lagaan = media.Movie("Lagaan", "The people of a small village in Victorian India stake their future on a game of cricket against their ruthless British rulers.",
                             "https://upload.wikimedia.org/wikipedia/en/b/b6/Lagaan.jpg",
                             "https://www.youtube.com/watch?v=oSIGQ0YkFxs",  "2001", "224 Minutes", "Hindi","(8.2/10)" )


movies = [taare_zameen_par,  three_idiots, lagaan, the_italian_job, the_avengers, the_transporter, the_chronicles_of_narnia, madagascar, the_hobbit]
fresh_tomatoes.open_movies_page(movies)
