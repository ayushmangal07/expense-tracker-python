from database import conn, cursor
import matplotlib.pyplot as plt

def category_pie_chart():    
    query = """
SELECT category,
       SUM(amount)
FROM expenses
GROUP BY category
ORDER BY SUM(amount) DESC
"""
    cursor.execute(query)

    records = cursor.fetchall()
    if not records:
        print("No records found.")
        return
    
    categories = []
    amounts = []

    for row in records:

        categories.append(row[0])
        amounts.append(float(row[1]))
    plt.figure(figsize=(8, 6))

    plt.pie(
    amounts,
    labels=categories,
    autopct="%1.1f%%",
    startangle=90
    )

    plt.title("Expense Distribution by Category")

    plt.tight_layout()

    plt.show()



def category_bar_chart():    
    query = """
SELECT category,
       SUM(amount)
FROM expenses
GROUP BY category
ORDER BY SUM(amount) DESC
"""

    cursor.execute(query)

    records = cursor.fetchall()

    if not records:
        print("No records found.")
        return
    categories = []
    amounts = []

    for row in records:

        categories.append(row[0])
        amounts.append(float(row[1]))

    plt.figure(figsize=(8, 6))

    plt.bar(categories, amounts)

    plt.title("Expense by Category")

    plt.xlabel("Category")

    plt.ylabel("Amount (₹)")
    
    plt.tight_layout()

    plt.show()



def monthly_expense_analysis():

    query = """
    SELECT YEAR(expense_date),
        MONTH(expense_date),
        SUM(amount)
    FROM expenses
    GROUP BY YEAR(expense_date),
            MONTH(expense_date)
    ORDER BY YEAR(expense_date),
            MONTH(expense_date)
    """

    cursor.execute(query)

    records = cursor.fetchall()

    if not records:
        print("\nNo records found.\n")
        return

    month_names = {
        1: "Jan",
        2: "Feb",
        3: "Mar",
        4: "Apr",
        5: "May",
        6: "Jun",
        7: "Jul",
        8: "Aug",
        9: "Sep",
        10: "Oct",
        11: "Nov",
        12: "Dec"
    }

    months = []
    amounts = []

    for row in records:

        year = row[0]
        month = row[1]
        total = row[2]

        months.append(f"{month_names[month]} {year}")
        amounts.append(float(total))

    plt.figure(figsize=(10, 6))

    plt.plot(
        months,
        amounts,
        marker="o",
        linewidth=2
    )

    plt.title("Monthly Expense Analysis")

    plt.xlabel("Month")

    plt.ylabel("Total Expense (₹)")

    plt.grid(True)

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.show()