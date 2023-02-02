from films_connect import * 
from read_films import read_film
from time import sleep

def update_film():
    idField = input("Enter the ID for the record to be updated: ")

    # enter the name of the field to be updated 
    fieldName = input("Which field would you like to update: (Title, Year Released, Rating, Duration, Genre)?")
    fieldName = fieldName.replace(" ", "")
    
    print(fieldName)
    newFieldValue = input(f"Enter the value for the {fieldName} ")
    print(f"User Value {newFieldValue}")
    newFieldValue = "'" + newFieldValue + "'"
    print(f"User Value with single quote added {newFieldValue}")
    cursor.execute("UPDATE Films SET " + fieldName + "=" + newFieldValue + "WHERE filmID = " + idField)
    conn.commit()
    print(f"Record {idField} Updated")

    sleep(2)
    read_film() 

if __name__ == "__main__":
    update_film()

