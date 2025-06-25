class Watchlist:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)
        print(f"'{movie}' was added to your watchlist.")

    def remove_movie(self, movie):
        if movie in self.movies:
            self.movies.remove(movie)
            print(f"'{movie}' was removed from your watchlist.")
        else:
            print(f"'{movie}' is not in your watchlist.")
