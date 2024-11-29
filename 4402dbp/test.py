import sqlite3

def test_queries():
    conn = sqlite3.connect('movie_theater.db')
    cursor = conn.cursor()

    # Query 1: List all movies and their genres
    print("Query 1: Movies and Genres")
    cursor.execute("""
        SELECT Movies.title, Genre.genreName
        FROM Movies
        JOIN Genre ON Movies.genre_ID = Genre.genre_ID
    """)
    for row in cursor.fetchall():
        print(row)

    # Query 2: List all customers and their membership types
    print("\nQuery 2: Customers and Memberships")
    cursor.execute("""
        SELECT Customer.name, Membership.type
        FROM Customer
        JOIN Membership ON Customer.membership_ID = Membership.membership_ID
    """)
    for row in cursor.fetchall():
        print(row)

    # Query 3: Find all employees earning above $15.00
    print("\nQuery 3: Employees earning above $15.00")
    cursor.execute("""
        SELECT name, position, wage
        FROM Employee
        WHERE wage > 15.00
    """)
    for row in cursor.fetchall():
        print(row)

    # Query 4: List all tickets purchased by a specific customer
    print("\nQuery 4: Tickets purchased by customer ID 1")
    cursor.execute("""
        SELECT * 
        FROM Tickets 
        WHERE customer_ID = 1
    """)
    for row in cursor.fetchall():
        print(row)

    # Query 5: Retrieve all movies being shown at a specific theater
    print("\nQuery 5: Movies shown at a theater")
    cursor.execute("""
        SELECT Movies.title, Theater.location
        FROM Movies
        JOIN MovieTime ON Movies.movie_ID = MovieTime.movietime_ID
        JOIN Theater ON Theater.theater_ID = MovieTime.movietime_ID
    """)
    for row in cursor.fetchall():
        print(row)

    conn.close()

if __name__ == "__main__":
    test_queries()

