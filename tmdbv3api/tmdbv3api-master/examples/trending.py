from tmdbv3api import TMDb, Trending

tmdb = TMDb()

tmdb.api_key = "af9ff4b1596689f894e8c29ca58dcc61"

trending = Trending()

# What are the TV shows trending today?
shows= trending.tv_day()

for p in shows:
    print(p.name)
    print(p.overview)

# What are the Movies trending this week?
movies = trending.movie_week()

for p in movies:
    print(p.name)
    print(p.overview)
