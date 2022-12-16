from tmdbv3api import TMDb, Discover

tmdb = TMDb()

tmdb.api_key = "af9ff4b1596689f894e8c29ca58dcc61"

discover = Discover()

# What are the most popular TV shows?

show = discover.discover_tv_shows({"sort_by": "popularity.desc"})

for p in show:
    print(p.name)
    print(p.overview)
    print("")
