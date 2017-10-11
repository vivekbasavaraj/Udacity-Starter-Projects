import webbrowser

class Movie():
    """ This class gives information about the movies"""
    #this function is the constructor of the class, it initialises a spaces inside the memory
    def __init__(self, movie_title, movie_storyline, poster_image, youtube_trailer, movie_year, movie_running_time, movie_language, movie_imdb_rating):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = youtube_trailer
        self.year = movie_year
        self.running_time = movie_running_time
        self.language = movie_language
        self.imdb_rating = movie_imdb_rating

        
