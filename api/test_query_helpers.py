# %%
from database import SessionLocal
import api.query_helpers as query_helpers

# Créer une session
db = SessionLocal()

# %%
# Tester la récupération de films
movies = query_helpers.get_movies(db, limit=5, genre="Comedy")

for movie in movies:
    print(f"ID: {movie.movieId}, Titre: {movie.title}, Genres: {movie.genres}")

# %%
# Fermer la session
db.close()