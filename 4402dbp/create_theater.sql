CREATE TABLE Movies (
    movies_ID INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    genre_ID INTEGER,
    rating TEXT,
    FOREIGN KEY (genre_ID) REFERENCES Genre(genre_ID)
);

CREATE TABLE MovieTime (
    movie_ID INTEGER,
    start_time TEXT NOT NULL,
    movie_length INTEGER NOT NULL,
    day TEXT NOT NULL,
    PRIMARY KEY (movie_ID, start_time, day), 
    FOREIGN KEY (movie_ID) REFERENCES Movies(movies_ID)
);

CREATE TABLE Seat (
    theater_ID INTEGER,
    seat_number INTEGER,
    row_letter TEXT NOT NULL,
    PRIMARY KEY (theater_ID, seat_number, row_letter), 
    FOREIGN KEY (theater_ID) REFERENCES Theater(theater_ID)
);

CREATE TABLE Customer (
    customer_ID INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    membership_ID INTEGER,
    FOREIGN KEY (membership_ID) REFERENCES Membership(membership_ID)
);

CREATE TABLE Genre (
    genre_ID INTEGER PRIMARY KEY,
    genre_name TEXT NOT NULL
);

CREATE TABLE Employee (
    employee_ID INTEGER PRIMARY KEY,
    position TEXT NOT NULL,
    name TEXT NOT NULL,
    wage REAL
);

CREATE TABLE Theater (
    theater_ID INTEGER PRIMARY KEY,
    room TEXT NOT NULL
);

CREATE TABLE Membership (
    membership_ID INTEGER PRIMARY KEY,
    membership_name TEXT NOT NULL
);
