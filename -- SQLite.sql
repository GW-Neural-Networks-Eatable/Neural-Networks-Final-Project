-- SQLite
CREATE TABLE Restaurant(
NAME    TEXT    PRIMARY KEY NOT NULL,
CITY    TEXT    NOT NULL,
STATE   TEXT    NOT NULL
);

CREATE TABLE Dish(
RESTAURANT    TEXT    PRIMARY KEY NOT NULL,
DISH_NAME     TEXT    NOT NULL,
PATH          TEXT    NOT NULL, --IMAGE PATH
PRICE         REAL    NOT NULL
); 

