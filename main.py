from core.watchlist import Watchlist
from invoker.command_invoker import CommandInvoker
from commands.add_movie import AddMovieCommand
from commands.remove_movie import RemoveMovieCommand

if __name__ == "__main__":
    watchlist = Watchlist()
    invoker = CommandInvoker()

    invoker.run_command(AddMovieCommand(watchlist, "Inception"))
    invoker.run_command(AddMovieCommand(watchlist, "The Matrix"))
    invoker.run_command(RemoveMovieCommand(watchlist, "Inception"))
    invoker.run_command(RemoveMovieCommand(watchlist, "Final Destination"))

    print("\nCurrent Watchlist:", watchlist.movies)
