CREATE DATABASE eLib DEFAULT CHARACTER SET utf8; //It creates the database

USE E-Library; //it goes into the database

CREATE TABLE Books{ //crestes a table with a the following columns
    id MEDIUMINT NOT NUL AUTO-INCREMENT,
    name CHAR(100) NOT NULL,
    path CHAR(200) NOT NULL,
    path_to_cover CHAR(200),
    driveLink CHAR(500);

    //if the answer is yes than it's equal to 1, else it's equal to 0
    ebook TINYINT,
    pdf TINYINT,
    fiction TINYINT,
    mystery TINYINT,
    fantasy TINYINT,
    science_fiction TINYINT,
    non-fiction TINYINT,
    genre_fiction TINYINT,
    thriller TINYINT,
    romance TINYINT,
    young_adult_fiction TINYINT,
    crime_fiction TINYINT,
    literary_fiction TINYINT,
    horror_fiction TINYINT,
    history TINYINT,
    fairy_tale TINYINT,
    comic_book TINYINT,
    manga TINYINT,
    light_novel TINYINT
    classic TINYINT
};


//Now to add a Book

INSERT INTO Books (name, path, path_to_cover, ebook, pdf, fiction, mystery, fantasy, science_fiction, non-fiction, genre_fiction, thriller, romance, young_adult_fiction, crime_fiction, literary_fiction, horror_fiction, history, fairy_tale, comic_book, manga, light_novel, classic) VALUES (a,b,c,...)
