class Movie:
    def __init__(self, title, director, year):
        self.title = title
        self.director = director
        self.year = year

    def result(self):
        return '{} {} {}'.format(self.title, self.director, self.year)


# objects of the class Movie
titanic = Movie('Titanic', 'James Cameron', 1997)
star_wars = Movie('Star Wars', 'George Lucas', 1977)
fight_club = Movie('Fight Club', 'David Fincher', 1999)

titanic.result()
star_wars.result()
fight_club.result()
