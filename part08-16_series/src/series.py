class Series:
    def __init__(self, title, seasons, genre):
        self.title = title
        self.seasons = seasons
        self.genre = genre
        self.ratings = []

    def __str__(self):
        reviews = "no ratings"
        if len(self.ratings) > 0:
            reviews = f"{len(self.ratings)} ratings, average {sum(self.ratings) / len(self.ratings):.1f} points"
        return (
            f"{self.title} ({self.seasons} seasons)\n"
            f'genres: {", ".join(self.genre)}\n'
            f"{reviews}"
        )

    def rate(self, rating: int):
        self.ratings.append(rating)


def minimum_grade(rating: float, seriesList: list):
    result = []
    for series in seriesList:
        if sum(series.ratings) / len(series.ratings) >= rating:
            result.append(series)

    return result


def includes_genre(genre: str, seriesList: list):
    result = []
    for series in seriesList:
        if genre in series.genre:
            result.append(series)

    return result


if __name__ == '__main__':
    dexter = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    dexter.rate(4)
    dexter.rate(5)
    dexter.rate(5)
    dexter.rate(3)
    dexter.rate(0)
    print(dexter)

    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)

    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)

    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)

    series_list = [s1, s2, s3]

    print("a minimum grade of 4.5:")
    for series in minimum_grade(4.5, series_list):
        print(series.title)

    print("genre Comedy:")
    for series in includes_genre("Comedy", series_list):
        print(series.title)
