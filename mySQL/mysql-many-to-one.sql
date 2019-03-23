CREATE TABLE Series (
  series_id INTEGER NOT NULL  AUTO_INCREMENT PRIMARY KEY,
  series_name VARCHAR(250)
 );

CREATE TABLE Languages(
  language_id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
  language_name VARCHAR(100)
);

CREATE TABLE Authors(
  Author_id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
  Author_name VARCHAR(100),

  INDEX USING BTREE (Author_name)
);

CREATE TABLE Books(
  book_id  INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
  book_name VARCHAR(250) NOT NULL,
  book_path VARCHAR(250) NOT NULL,
  fiction TINYINT,
  mystery TINYINT,
  fantasy TINYINT,
  science_fiction TINYINT,
  non_fiction TINYINT,
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
  light_novel TINYINT,
  classic TINYINT,

  series_id INTEGER,
  Author_id INTEGER,
  language_id INTEGER,

  INDEX USING BTREE (book_name),

  CONSTRAINT FOREIGN KEY (series_id) REFERENCES Series(series_id),
  CONSTRAINT FOREIGN KEY (Author_id) REFERENCES Authors(Author_id),
  CONSTRAINT FOREIGN KEY (language_id) REFERENCES Languages(language_id)

);
