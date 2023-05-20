import mysql.connector

# Database connection
mydb = mysql.connector.connect(
    
  host="localhost",
  user="root",
  password="chintu123",
  database="mydata"
)
mycursor = mydb.cursor()

# Banker module
class Banker:
    def register_customer(self, name, email, password, balance):
        query = "INSERT INTO customers (name, email, password, balance) VALUES (%s, %s, %s, %s)"
        values = (name, email, password, balance)
        mycursor.execute(query, values)
        mydb.commit()
        print("Customer registered successfully.")

    def login(self, email, password):
        query = "SELECT * FROM customers WHERE email = %s AND password = %s"
        values = (email, password)
        mycursor.execute(query, values)
        result = mycursor.fetchone()
        if result:
            print("Login successful.")
        else:
            print("Invalid email or password.")

    def update_customer(self, customer_id, name, email, password, balance):
        query = "UPDATE customers SET name = %s, email = %s, password = %s, balance = %s WHERE id = %s"
        values = (name, email, password, balance, customer_id)
        mycursor.execute(query, values)
        mydb.commit()
        print("Customer updated successfully.")

    def view_customers(self):
        query = "SELECT * FROM customers"
        mycursor.execute(query)
        customers = mycursor.fetchall()
        for customer in customers:
            print(f"ID: {customer[0]}, Name: {customer[1]}, Email: {customer[2]}, Balance: {customer[4]}")

    def delete_customers(self):
        query = "DELETE FROM customers"
        mycursor.execute(query)
        mydb.commit()
        print("All customers deleted successfully.")

# Customer module
class Customer:
    def register(self, name, email, password, balance):
        query = "INSERT INTO customers (name, email, password, balance) VALUES (%s, %s, %s, %s)"
        values = (name, email, password, balance)
        mycursor.execute(query, values)
        mydb.commit()
        print("Customer registered successfully.")

    def login(self, email, password):
        query = "SELECT * FROM customers WHERE email = %s AND password = %s"
        values = (email, password)
        mycursor.execute(query, values)
        result = mycursor.fetchone()
        if result:
            print("Login successful.")
        else:
            print("Invalid email or password.")

    def withdraw(self, customer_id, amount):
        query = "SELECT balance FROM customers WHERE id = %s"
        values = (customer_id,)
        mycursor.execute(query, values)
        result = mycursor.fetchone()
        if result:
            balance = result[0]
            if balance >= amount:
                updated_balance = balance - amount
                query = "UPDATE customers SET balance = %s WHERE id = %s"
                values = (updated_balance, customer_id)
                mycursor.execute(query, values)
                mydb.commit()
                print("Amount withdrawn successfully.")
            else:
                print("Insufficient balance.")
        else:
            print("Invalid customer ID.")

    def deposit(self, customer_id, amount):
        query = "SELECT balance FROM customers WHERE id = %s"
        values = (customer_id,)
        mycursor.execute(query, values)
        result = mycursor.fetchone()
        if result:
            balance = result[0]
            updated_balance = balance + amount
            query = "UPDATE customers SET balance = %s WHERE id = %s"
            values = (updated_balance, customer_id)
            mycursor.execute(query, values)
            mydb.commit()
            print("Amount deposited successfully.")
        else:
            print("Invalid customer ID.")

    def view_balance(self, customer_id):
        query = "SELECT balance FROM customers WHERE id = %s"
        values = (customer_id,)
        mycursor.execute(query, values)
        result = mycursor.fetchone()
        if result:
            print(f"Your balance: {result[0]}")
        else:
            print("Invalid customer ID.")


# Main program
banker = Banker()
customer = Customer()

while True:
    print("1. Banker")
    print("2. Customer")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        print("1. Register Customer")
        print("2. Login")
        print("3. Update Customer")
        print("4. View Customers")
        print("5. Delete Customers")
        banker_choice = input("Enter your choice: ")

        if banker_choice == "1":
            name = input("Enter customer name: ")
            email = input("Enter customer email: ")
            password = input("Enter customer password: ")
            balance = float(input("Enter initial balance: "))
            banker.register_customer(name, email, password, balance)

        elif banker_choice == "2":
            email = input("Enter customer email: ")
            password = input("Enter customer password: ")
            banker.login(email, password)

        elif banker_choice == "3":
            customer_id = int(input("Enter customer ID: "))
            name = input("Enter updated name: ")
            email = input("Enter updated email: ")
            password = input("Enter updated password: ")
            balance = float(input("Enter updated balance: "))
            banker.update_customer(customer_id, name, email, password, balance)

        elif banker_choice == "4":
            banker.view_customers()

        elif banker_choice == "5":
            banker.delete_customers()

    elif choice == "2":
        print("1. Register")
        print("2. Login")
        print("3. Withdraw Amount")
        print("4. Deposit Amount")
        print("5. View Balance")
        customer_choice = input("Enter your choice: ")

        if customer_choice == "1":
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            balance = float(input("Enter initial balance: "))
            customer.register(name, email, password, balance)

        elif customer_choice == "2":
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            customer.login(email, password)

        elif customer_choice == "3":
            customer_id = int(input("Enter your customer ID: "))
            amount = float(input("Enter amount to withdraw: "))
            customer.withdraw(customer_id, amount)

        elif customer_choice == "4":
            customer_id = int(input("Enter your customer ID: "))
            amount = float(input("Enter amount to deposit: "))
            customer.deposit(customer_id, amount)

        elif customer_choice == "5":
            customer_id = int(input("Enter your customer ID: "))
            customer.view_balance(customer_id)

    elif choice == "3":
        break

mydb.close()
