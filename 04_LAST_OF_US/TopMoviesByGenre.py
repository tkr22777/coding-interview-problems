from typing import List, Tuple
from collections import defaultdict

def top_movies_by_genre(movies: List[Tuple[str, float, str]]) -> dict:
    top_movies_by_g = defaultdict(lambda: (-1, ""))
    for title, rating, genre in movies:
        highest_rating, _ = top_movies_by_g[genre]
        if rating > highest_rating:
            top_movies_by_g[genre] = (rating, title)
    
    response_map = {}
    for genre, (_, title) in top_movies_by_g.items():
        response_map[genre] = title
    return response_map

# Test cases
movies = [
    ("Inception", 8.8, "Sci-Fi"),
    ("The Matrix", 8.7, "Sci-Fi"),
    ("Interstellar", 8.6, "Sci-Fi"),
    ("The Godfather", 9.2, "Crime"),
    ("Pulp Fiction", 8.9, "Crime"),
    ("The Dark Knight", 9.0, "Action"),
    ("Mad Max: Fury Road", 8.1, "Action"),
    ("Parasite", 8.6, "Thriller")
]
top_movies_by_g = top_movies_by_genre(movies=movies)
print(top_movies_by_g) 