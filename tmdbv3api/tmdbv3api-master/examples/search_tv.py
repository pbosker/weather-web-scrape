from tmdbv3api import TMDb, TV

tmdb = TMDb()

tmdb.api_key = "af9ff4b1596689f894e8c29ca58dcc61"

tv = TV()

tvshow=input("Enter a TV show:  ")
show = tv.search(tvshow)

for result in show:
    print(result.name)
    print(result.overview)
