# MovieLens SDK - `moviessdk`

A simple Python SDK for interacting with the MovieLens REST API. It is designed for **Data Analysts** and **Data Scientists**, with native support for **Pydantic**, **dictionaries** and **DataFrames Pandas**.

[![PyPI version](https://badge.fury.io/py/moviesdk.svg)](https://badge.fury.io/py/moviesdk)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
---

## Installation
```bash
pip install moviessdk
```
---

## Configuration
```python
from moviessdk import MovieClient, MovieConfig

# Configuration with the URL of your API (Render or local)
config = MovieConfig(movie_base_url="https://movielens-api-6zzm.onrender.com")
client = MovieClient(config=config)
```
---

## Testing the SDK
### 1. Health check

```python
client.health_check()
# Retourne : {"status": "ok"}
```

### 2. Retrieve movie
```python
movie = client.get_movie(1)
print(movie.title)
```

### 3. List of movies in DataFrame format
```python
df = client.list_movies(limit=5, output_format="pandas")
print(df.head())
```

---

## Available output modes
All list methods (`list_movies`, `list_ratings`, etc.) can return :

- **Pydantic** objects
- **dictionaries**
- **PandasDataFrames**

Example :

```python
client.list_movies(limit=10, output_format="dict")
client.list_ratings(limit=10, output_format="pandas")
```

---

## Local testing
You can also use a local API :

```python
config = MovieConfig(movie_base_url="http://localhost:8000")
client = MovieClient(config=config)
```
---

## Useful links
- API Render : [https://movielens-api-6zzm.onrender.com](https://movielens-api-6zzm.onrender.com)
- PyPI : [https://pypi.org/project/moviessdk](https://pypi.org/project/moviessdk)

---

## Licence
MIT License

## 👨‍💻​ Author
[Desty MPASSI](https://github.com/DestyM)