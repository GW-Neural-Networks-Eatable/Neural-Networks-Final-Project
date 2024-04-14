-- SQLite
-- sqlite3 testDB.db ".read schema.sql"
CREATE TABLE Restaurant(
    NAME    TEXT    PRIMARY KEY NOT NULL,
    CITY    TEXT    NOT NULL
);

CREATE TABLE Dish(
    RESTAURANT    TEXT    PRIMARY KEY NOT NULL,
    DISH_NAME     TEXT    NOT NULL,
    PATH          TEXT    NOT NULL,
    PRICE         REAL    NOT NULL
); 

