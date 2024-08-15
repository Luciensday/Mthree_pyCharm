from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

# SQLAlchemy connection and configuration
db_config = {
    'user': 'root',
    'password': 'Istoday92!',
    'host': 'localhost',
    'database': 'Aug13'
}

# Create the engine and session
engine = create_engine(f"mysql+pymysql://{db_config['user']}:{db_config['password']}@{db_config['host']}/{db_config['database']}")
Session = sessionmaker(bind=engine)
session = Session()

# CRUD Operations using raw SQL queries
def display():
    sql_query = text("SELECT * FROM users")
    result = session.execute(sql_query)
    for row in result:
        print(row.id, row.name, row.email)

def search():
    id = input("Enter the id you want to search = ")
    sql_query = text("SELECT * FROM users WHERE id = :id")
    result = session.execute(sql_query, {"id": id}).fetchone()
    if result:
        print(result.id, result.name, result.email)
    else:
        print("User not found")

def insertData():
    name = input("Enter the name = ")
    email = input("Enter the email = ")
    sql_query = text("INSERT INTO users (name, email) VALUES (:name, :email)")
    session.execute(sql_query, {"name": name, "email": email})
    session.commit()
    print("User successfully added")

def updateData():
    id = input("Enter the id you want to update = ")
    ch = int(input("1 Update Name 2 Update Email"))
    if ch == 1:
        name = input("Enter the name = ")
        sql_query = text("UPDATE users SET name = :name WHERE id = :id")
        session.execute(sql_query, {"name": name, "id": id})
        print("Name successfully updated")
    elif ch == 2:
        email = input("Enter the email = ")
        sql_query = text("UPDATE users SET email = :email WHERE id = :id")
        session.execute(sql_query, {"email": email, "id": id})
        print("Email successfully updated")
    else:
        print("Invalid choice")
    session.commit()

def deleteData():
    id = input("Enter the id you want to delete = ")
    sql_query = text("DELETE FROM users WHERE id = :id")
    session.execute(sql_query, {"id": id})
    session.commit()
    print("User successfully deleted")



# Main loop
while True:
    print("1 Create record 2 Update record 3 Delete record 4 Display record 5 Search 6 Exit")
    ch = int(input("Enter the choice = "))
    match ch:
        case 1: insertData()
        case 2: updateData()
        case 3: deleteData()
        case 4: display()
        case 5: search()
        case 6: break
        case _: print("Invalid choice")

# Close the session when done
session.close()