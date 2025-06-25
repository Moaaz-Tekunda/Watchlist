from core.command_interface import Command
class RemoveMovieCommand(Command):
    def __init__(self, watchlist, movie):
        self.watchlist = watchlist
        self.movie = movie

    def execute(self):
        self.watchlist.remove_movie(self.movie)
