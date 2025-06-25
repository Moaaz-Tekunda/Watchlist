def add_movie(title: str, year: int, genre: str = "") -> None:
    """Add a movie to the watchlist."""
    print(f"Added movie: {title} ({year}) with Genre: {genre}")


def remove_movie(title: str) -> None:
    """Remove a movie from the watchlist."""
    print(f"Removed movie: {title}")

def edit_movie(title: str, new_title: str = None, new_year: int = None, new_genre: str = None) -> None:
    """Edit details of a movie in the watchlist."""
    changes = []
    if new_title:
        changes.append(f"Title changed to {new_title}")
    if new_year:
        changes.append(f"Year changed to {new_year}")
    if new_genre:
        changes.append(f"Genre changed to {new_genre}")
    
    change_summary = ", ".join(changes) #collect changes into a summary string
    print(f"Edited movie: {title}. Changes: {change_summary}")


