from films_connect import *




def read_film():
    cursor.execute("SELECT * FROM Films")
    row = cursor.fetchall()
    for record in row:
        print(record)
      
if __name__== "__main__":
    read_film()