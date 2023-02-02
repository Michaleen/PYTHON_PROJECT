from films_connect import *  # import the connect library
from time import sleep
from read_films import read_film


def delete_film():
    idField = input("Enter the ID number of the film to be deleted: ")

    # delete songs  by id
    cursor.execute(f"DELETE FROM Films WHERE filmID = {idField}")
    conn.commit()

    print(f"Film: {idField} deleted from the Films table in the database")
    sleep(3)

    read_film()

if __name__ == "__main__":
    delete_film()
