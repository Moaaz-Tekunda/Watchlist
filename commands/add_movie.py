from core.command_interface import Command

class AddMovieCommand(Command):
    def __init__(self, watchlist, movie):
        self.watchlist = watchlist
        self.movie = movie

    def execute(self):
        self.watchlist.add_movie(self.movie)
