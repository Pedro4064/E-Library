CREATE DATABASE eLib DEFAULT CHARACTER SET utf8; /*It creates the database*/

USE eLib; /*it goes into the database*/

CREATE TABLE Books( /*crestes a table with a the following columns*/

    id MEDIUMINT NOT NULL AUTO_INCREMENT,
    name CHAR(100) NOT NULL,
    path CHAR(200) NOT NULL,
    path_to_cover CHAR(200),
    driveLink CHAR(500);

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
);

-- Database to store a list of the physical books in the library
CREATE TABLE physicalBooks(
  id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR (200),
  available INTEGER,

  INDEX USING BTREE (name)

);

-- Label to log the info of those who rent a book 
CREATE TABLE Log(
  studentId INTEGER NOT NULL,
  bookTitle VARCHAR (200),
  rental_Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP 

);