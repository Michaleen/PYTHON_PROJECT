from films_connect import *

cursor.execute(
    """

CREATE TABLE "Films" (
    "filmID" integer,
    "title" text,
    "yearReleased" integer,
    "rating" text,
    "duration" integer,
    "genre" text,
    primary key ("filmID" AUTOINCREMENT)
    )
"""
)






# Database name filmflix.db 

# Table name tblfilms 

# filmID(integer), title(text), yearReleased(integer),rating(text),duration(integer),genre(text) 