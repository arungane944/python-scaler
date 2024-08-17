marvel_movies = {"deadpool", "The Avengers", "Thor", "Captain America", "Black Panther", "Doctor Strange", "Spider-Man: Homecoming"}
dc_movies = {"deadpool", "Batman v Superman", "Wonder Woman", "Aquaman", "Justice League", "Shazam!", "The Dark Knight"}

for movies in marvel_movies.difference(dc_movies):
    print(movies)

print("================================")
for movies in dc_movies.difference(marvel_movies):
    print(movies)
# won't include common movies and dc movies
