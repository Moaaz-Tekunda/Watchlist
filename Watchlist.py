def add_movie(title: str, year: int, genre: str = "") -> None:
    """Add a movie to the watchlist."""
    print(f"Added movie: {title} ({year}) with Genre: {genre}")


def remove_movie(title: str) -> None:
    """Remove a movie from the watchlist."""
    print(f"Removed movie: {title}")
    