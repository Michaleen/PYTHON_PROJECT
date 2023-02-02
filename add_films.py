from films_connect import *
from time import *
from read_films import read_film

def add_film():
    films = []
    #filmID = cursor.lastrowid
    title = input("Enter the film title")
    yearReleased = input("Enter the year released")
    rating = input("Enter the film rating")
    duration = input("Enter the film duration")
    genre = input("Enter the film genre")

    #films.append(filmID)
    films.append(title)
    films.append(yearReleased)
    films.append(rating)
    films.append(duration)
    films.append(genre)


    cursor.execute("INSERT INTO Films VALUES(null,?,?,?,?,?)", films)
    conn.commit()
    print(f"{title} has been added to the Films Table")
    sleep(3)
    read_film()

if __name__ == "__main__":
    add_film()
