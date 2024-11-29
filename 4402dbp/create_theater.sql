CREATE TABLE Movies (
    movie_ID INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    genre_ID INTEGER,
    rating TEXT,
    FOREIGN KEY (genre_ID) REFERENCES Genre(genre_ID)
);

CREATE TABLE Genre (
    genre_ID INTEGER PRIMARY KEY,
    genreName TEXT NOT NULL
);

CREATE TABLE Membership (
    membership_ID INTEGER PRIMARY KEY,
    type TEXT NOT NULL
);

CREATE TABLE Customer (
    customer_ID INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    membership_ID INTEGER,
    FOREIGN KEY (membership_ID) REFERENCES Membership(membership_ID)
);

CREATE TABLE Theater (
    theater_ID INTEGER PRIMARY KEY ,
    location TEXT NOT NULL
);

CREATE TABLE Employee (
    employee_ID INTEGER PRIMARY KEY ,
    position TEXT NOT NULL,
    name TEXT NOT NULL,
    wage REAL
);

CREATE TABLE MovieTime (
    movietime_ID INTEGER PRIMARY KEY,
    start_time TEXT NOT NULL,
    day TEXT NOT NULL,
    movielength INTEGER NOT NULL
);

CREATE TABLE Tickets (
    ticket_ID INTEGER PRIMARY KEY,
    customer_ID INTEGER,
    movie_time TEXT,
    movie_name TEXT,
    price REAL,
    seats INTEGER,
    FOREIGN KEY (customer_ID) REFERENCES Customer(customer_ID)
);

CREATE TABLE Seat (
    seat_num INTEGER PRIMARY KEY,
    row_letter TEXT NOT NULL
);

CREATE TABLE Rating (
    rating_ID INTEGER PRIMARY KEY,
    movies TEXT NOT NULL
);
