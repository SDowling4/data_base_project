import sqlite3

def view_movies():
    conn = sqlite3.connect('movie_theater.db')
    cursor = conn.cursor()
    cursor.execute("SELECT movie_ID, title, rating FROM Movies")
    movies = cursor.fetchall()
    print("\nMovies Available:")
    for movie in movies:
        print(f"ID: {movie[0]}, Title: {movie[1]}, Rating: {movie[2]}")
    conn.close()

def add_customer():
    conn = sqlite3.connect('movie_theater.db')
    cursor = conn.cursor()
    name = input("Enter customer name: ")
    email = input("Enter customer email: ")
    membership_id = input("Enter membership ID: ")
    cursor.execute(
        "INSERT INTO Customer (name, email, membership_ID) VALUES (?, ?, ?)",
        (name, email, membership_id)
    )
    conn.commit()
    print("Customer added successfully!")
    conn.close()

def main_menu():
    while True:
        print("\nMovie Theater CLI")
        print("1. View Movies")
        print("2. Add Customer")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            view_movies()
        elif choice == "2":
            add_customer()
        elif choice == "3":
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main_menu()
