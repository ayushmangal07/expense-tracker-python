from database import conn, cursor

def show_statistics():
    cursor.execute("SELECT COUNT(*) FROM expenses")
    count = cursor.fetchone()[0]

    if count == 0:
        print("\nNo expenses available.\n")
        return
    
    cursor.execute("SELECT SUM(amount) FROM expenses")
    total = cursor.fetchone()[0]

    cursor.execute("SELECT AVG(amount) FROM expenses")
    average = cursor.fetchone()[0]

    cursor.execute("SELECT MAX(amount) FROM expenses")
    maximum = cursor.fetchone()[0]

    cursor.execute("SELECT MIN(amount) FROM expenses")
    minimum = cursor.fetchone()[0]

    print("\n===== STATISTICS =====\n")

    print(f"Total Expense: ₹{total:.2f}")
    print(f"Average Expense: ₹{average:.2f}")

    print(f"Highest Expense: ₹{maximum:.2f}")
    print(f"Lowest Expense: ₹{minimum:.2f}")
    print(f"Total Transactions: {count}")



def category_statistics():

    query = """
    SELECT category,
           SUM(amount),
           COUNT(*)
    FROM expenses
    GROUP BY category
    ORDER BY SUM(amount) DESC
    """

    cursor.execute(query)

    records = cursor.fetchall()

    if not records:
        print("No records found.")
        return

    print("\n===== CATEGORY STATISTICS =====\n")

    for row in records:

        print(f"""
Category      : {row[0]}
Total Spent   : ₹{row[1]}
Transactions  : {row[2]}
-------------------------
""")