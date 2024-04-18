-- SQLBook: Code
-- sqlite3 testDB.db ".read schema.sql"
DROP TABLE IF EXISTS Restaurant; 
DROP TABLE IF EXISTS Dish; 

-- SQLite
CREATE TABLE Restaurant(
    NAME    TEXT    NOT NULL,
    URL     TEXT    Not NULL,
    CITY    TEXT    NOT NULL,
    STATE   TEXT    NOT NULL
);

CREATE TABLE Dish(
    RESTAURANT    TEXT    NOT NULL,
    DISH_NAME     TEXT    NOT NULL,
    PATH          TEXT    NOT NULL, --IMAGE PATH
    PRICE         REAL    NOT NULL,
    PRIMARY KEY (RESTAURANT, DISH_NAME)
); 

