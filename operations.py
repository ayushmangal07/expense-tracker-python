from database import conn, cursor
from datetime import datetime

def display_records(records):

    for row in records:

        print(f"""
ID: {row[0]}
Date: {row[1]}
Category: {row[2]}
Amount: ₹{row[3]}
Description: {row[4]}
-------------------------
""")
        


def add_expense():
    

    date = input("Enter Date (YYYY-MM-DD): ")
    try:
        datetime.strptime(date, "%Y-%m-%d")

    except ValueError:
        print("Invalid Date Format. Use YYYY-MM-DD")
        return 
    
    category = input("Enter Category: ").strip().title()

    try:
        amount = float(input("Enter Amount: "))

    except ValueError:
        print("Invalid Amount")
        return
    
    description = input("Enter Description: ").strip()

    if amount <= 0:
        print("Amount must be greater than zero")
        return

    query = """
    INSERT INTO expenses
    (expense_date, category, amount, description)
    VALUES (%s, %s, %s, %s)
    """

    values = (date, category, amount, description)

    cursor.execute(query, values)
    conn.commit()

    print("\nExpense Added Successfully!\n")



def view_expenses():

    cursor.execute("""
SELECT * FROM expenses
ORDER BY expense_date DESC
""")

    records = cursor.fetchall()

    if len(records) == 0:
        print("No expenses found.")
        return

    print("\n===== EXPENSE LIST =====")
    print(f"Total Records: {len(records)}\n")

    display_records(records)



def search_by_category():

    category = input("Enter Category: ").strip().title()

    query = """
    SELECT * FROM expenses
    WHERE category = %s
    """

    cursor.execute(query, (category,))

    records = cursor.fetchall()

    if len(records) == 0:
        print("\nNo records found.\n")
        return

    print(f"\nTotal Matches: {len(records)}\n")

    print("\nMatching Records:\n")

    display_records(records)
        


def search_by_date():

    date = input("Enter Date (YYYY-MM-DD): ")

    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("Invalid Date Format")
        return    

    query = """
    SELECT * FROM expenses
    WHERE expense_date = %s
    """

    cursor.execute(query, (date,))

    records = cursor.fetchall()

    if len(records) == 0:
        print("No records found.")
        return

    print(f"\nTotal Matches: {len(records)}\n")

    display_records(records)



def search_by_amount():

    try:
        minimum = float(input("Enter Minimum Amount: "))
        maximum = float(input("Enter Maximum Amount: "))
    except ValueError:
        print("Invalid Amount")
        return

    if minimum > maximum:
        print("Minimum amount cannot be greater than maximum amount.")
        return

    query = """
    SELECT * FROM expenses
    WHERE amount BETWEEN %s AND %s
    """

    cursor.execute(query, (minimum, maximum))

    records = cursor.fetchall()

    if len(records) == 0:
        print("\nNo Records Found\n")
        return

    print(f"\nTotal Matches: {len(records)}\n")

    display_records(records)



def search_menu():


    print("""
        ===== SEARCH MENU =====
        1. Search by Category
        2. Search by Date
        3. Search by Amount Range

        """)

    choice = input("Enter Choice: ")

    if choice == "1":
        search_by_category()

    elif choice == "2":
        search_by_date()
    
    elif choice == "3":
        search_by_amount()

    else:
        print("Invalid Choice")


        
def delete_expense():

    try:
        expense_id = int(input("Enter Expense ID to Delete: "))

    except ValueError:
        print("Invalid ID")
        return
    
    query = """
            SELECT * FROM expenses
            WHERE id = %s
            """

    cursor.execute(query, (expense_id,))

    record = cursor.fetchone()

    if not record:
        print("Expense Not Found")
        return
    
    print("\nExpense Found:\n")

    display_records([record])   

    confirm = input(
    "Are you sure you want to delete this expense? (y/n): "
    ).lower()
    if confirm!='y':
        print("Deletion Cancelled")
        return
    
    query = """
            DELETE FROM expenses
            WHERE id = %s
            """

    cursor.execute(query, (expense_id,))

    conn.commit()

    print("Expense Deleted Successfully!")



def update_expense():

    try:
        expense_id = int(input("Enter Expense ID: "))
    except ValueError:
        print("Invalid ID")
        return
    
    query = """
            SELECT * FROM expenses
            WHERE id = %s
            """

    cursor.execute(query, (expense_id,))

    record = cursor.fetchone()

    if not record:
        print("Expense Not Found")
        return
    
    print("\n\nCurrent Record:")

    display_records([record])

    new_date = input("Enter New Date (YYYY-MM-DD): ")
    try:
        datetime.strptime(new_date, "%Y-%m-%d")
    except ValueError:
        print("Invalid Date Format")
        return
    
    new_category = input("Enter New Category: ").strip().title()

    try:
        new_amount = float(input("Enter New Amount: "))
    except ValueError:
        print("Invalid Amount")
        return
    
    if new_amount <= 0:
        print("Amount must be greater than zero")
        return

    new_description = input("Enter New Description: ").strip()

    query = """
        UPDATE expenses
        SET expense_date = %s,
            category = %s,
            amount = %s,
            description = %s
        WHERE id = %s
        """
    values = (
    new_date,
    new_category,
    new_amount,
    new_description,
    expense_id
    )

    cursor.execute(query, values)

    conn.commit()
    print("\nExpense Updated Successfully!\n")