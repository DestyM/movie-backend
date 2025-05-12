# %%
from moviessdk import MovieClient, MovieConfig


# Initialisation du client avec l'URL de l'API
config = MovieConfig(movie_base_url="https://movielens-api-6zzm.onrender.com")
client = MovieClient(config=config)

# 1. Health check
print("Health check:")
print(client.health_check())


# %%
# 2. Récupérer un film par ID
print("\n Movie ID 1:")
movie = client.get_movie(1)
print(movie)
print(type(movie))


# %%
# 3. Lister les films (premiers 5)
print("\n List of movies:")
movies = client.list_movies(limit=5)
print(type(movies))
for m in movies:
    print(m)
    print(type(m))

# %%
# 4. Récupérer un rating spécifique
print("\n Rating for user 1 and movie 1:")
rating = client.get_rating(user_id=1, movie_id=1)
print(rating)
print(type(rating))


# %%
# 5. Lien du film
print("\n Link for movie ID 1:")
link = client.get_link(movie_id=1)
print(link)
print(type(link))


# %%
# 6. Analytics
print("\n Analytics:")
analytics = client.get_analytics()
print(analytics)
print(type(analytics))


# %%
# 7. Tests avec option du choix de format de sortie
    # Par défaut : objets Pydantic
new_movies = client.list_movies(limit=5)
print(new_movies)
print(type(new_movies))


# %%
    # Format dictionnaire
new_movies_dicts = client.list_movies(limit=5, output_format="dict")
print(new_movies_dicts)
print(type(new_movies_dicts))

 #%%
    # Format DataFrame
new_movies_df = client.list_movies(limit=5, output_format="pandas")
print(new_movies_df)
print(type(new_movies_df))
# %%
