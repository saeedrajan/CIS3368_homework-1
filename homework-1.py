from binhex import openrsrc
import re
import mysql.connector
from mysql.connector import Error
# to start the project I first built the menu. Then started to create the sql python functions that interacted with the database.
# After this I started to add the sub menu, depending on the use, like the update function should show the cars so the user could
# select the right car to update
#this the the main conection function
def conn_connection(hostname,connp, username, passwd, dbname):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = hostname,
            port = connp,
            user = username,
            password = passwd,
            database = dbname
        )
        print("Connection Success")
    except Error as e:
        print(f'The error {e}')
    return connection
conn = conn_connection()
curr = conn.cursor(dictionary = True)
#all data var holds the sql pramas
#this function interacts with the database
def add_car_db(make, model, year, color):
    sql = 'insert into garage values(null,%s,%s,%s,%s)'
    data = (make, model, year, color)
    curr.execute(sql,data)
    curr.execute('commit;')
#each of the menus options are it own functions
def add_car_menu():
    #this function displays the menu to enter the data to add a car and sends it to a database
    make = input("Enter Car make: ")
    model = input("Enter Car model: ")
    year = int(input("Enter Car year: "))
    color = input("Enter Car color: ")
    add_car_db(make, model, year, color)


def remove_car_db(id):
    sql = 'DELETE FROM garage WHERE id = %s;'
    data = [id]
    curr.execute(sql,data)
    curr.execute('commit;')

def remove_car_menu():
    #this function shows the current cars in the db and gives an option to delete
    sql = 'select * from garage'
    curr.execute(sql)
    rows = curr.fetchall()
    print("ID", "Make", "Model", "Year", "Color")
    for x in range(0, len(rows)):
        print(rows[x]["id"], rows[x]["make"],rows[x]["model"],rows[x]["year"],rows[x]["color"])
    remove_car_db(input("Enter car ID to remove: "))

def update_car(id, make, model, year, color):
    sql = "UPDATE table_name SET make = %s, model = %s, year = %s, color = %s WHERE id = %s;"
    data = (make, model, year, color, id)
    curr.execute(sql, data)
    curr.execute('commit;')

#this is and example of a sub menu what would diplay update options
def update_car_menu():
    #this function show the upadte menu to enter new data for the cars
    sql = 'select * from garage'
    curr.execute(sql)
    rows = curr.fetchall()
    print("ID", "Make", "Model", "Year", "Color")
    for x in range(0, len(rows)):
        print(rows[x]["id"], rows[x]["make"],rows[x]["model"],rows[x]["year"],rows[x]["color"])
    id = input("Enter car ID to update: ")
    make = input("Enter Car make: ")
    model = input("Enter Car model: ")
    year = int(input("Enter Car year: "))
    color = input("Enter Car color: ")
    update_car(id, make, model, year, color)

def show_all_sort():
    #this is the sore function it gets all the cars and sorts them by the year
    sql = "select * from garage order by year asc"
    curr.execute(sql)
    rows = curr.fetchall()
    print("ID", "Make", "Model", "Year", "Color")
    for x in range(0, len(rows)):
        print(rows[x]["id"], rows[x]["make"],rows[x]["model"],rows[x]["year"],rows[x]["color"])
def show_all_color(color):
    #this is the function that gets all the cars for a certin color
    sql = "select * from garage where color = %s"
    curr.execute(sql, [color])
    rows = curr.fetchall()
    print("ID", "Make", "Model", "Year", "Color")
    for x in range(0, len(rows)):
        print(rows[x]["id"], rows[x]["make"],rows[x]["model"],rows[x]["year"],rows[x]["color"])
#this is the main menu that show all the options
def show_menu():
    print("Menu")
    print("a - Add car")
    print("d - Remove car")
    print("u - Update car details")
    print("r1 - Output all cars sorted by year (ascending)")
    print("r2- Output all cars of a certain color")
    print("q - Quit")
# this is the main function that the excution starts from
while True:
    show_menu()
    option = input("Enter option: ")
    if(option == 'a'):
        add_car_menu()
    elif(option == 'd'):
        remove_car_menu()
    elif(option == 'u'):
        update_car_menu()
    elif(option == 'r1'):
        show_all_sort()
    elif(option == 'r2'):
        show_all_color(input("Enter the Color to sort by: "))
    elif(option == 'q'):
        break
