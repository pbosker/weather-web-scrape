from tmdbv3api import TMDb, Search

tmdb = TMDb()

tmdb.api_key = "af9ff4b1596689f894e8c29ca58dcc61"

search = Search()

#results = search.movies({"query": "Matrix", "year": 1999})
results = search.movies({"query": "Simpsons"})

for result in results:
    print(result.title)
    print(result.overview)
