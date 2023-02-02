from films_connect import * 
import time

# filter by film genre

def filter_genre():
    genre_options = {'1':'Drama', '2': 'Action', '3': 'Comedy', '4':'Crime', '5': 'Fantasy', '6':'Western', '7': 'Sci-Fi','8': 'Adventure', '9': 'Thriller', '10': 'Family'}
    options = 0 

    while options not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
        print("""\n
            1. Drama
            2. Action
            3. Comedy
            4. Crime
            5. Fantasy
            6. Western
            7. Sci-Fi
            8. Adventure
            9. Thriller
           10. Family"""
        )

        options = input("\nPlease enter the  Genre would you like to select? (1-10): ")

        if options not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:

            print("n\That selections is not available")
        
        else:
            break
    
    time.sleep(2)
    cursor.execute(f"SELECT * FROM Films WHERE genre = '{genre_options[options]}'")
    row = cursor.fetchall()
    for record in row:
        print(record)

# Filter by film rating

def filter_rating():
    rating_options = {'1': 'PG', '2': 'PG-13', '3': 'R', '4': 'Not Rated'}
    options = 0 

    while options not in ["1", "2", "3", "4"]:
        print("""\n
        
        1. PG
        2. PG-13
        3. R
        4. Not Rated"""
        )

        options = input("\nPlease enter the Rating you would like to select? (1-4): ")

        if options not in ["1", "2", "3", "4"]: 

            print("\nThat selections is not available")
        
        else:
            break

    time.sleep(2)
    cursor.execute(f"SELECT * FROM Films WHERE rating = '{rating_options[options]}'")
    row = cursor.fetchall()
    for record in row:
        print(record)


# Main Filter menu

def filter_film():
    options = 0

    while options not in ["1", "2"]:

        print("""\nHow would you like to filter your results:
                
                1. Genre
                2. Rating"""
                )

        options = input("\nPlease enter the corresponding number? (1-2): ")

        if options not in ["1", "2"]: 

            print("\nThat selections is not available")
        
        elif options == "1":
            filter_genre()
        
        elif options == "2":
            filter_rating()

if __name__ == "__main__":
    filter_film()
