from operations import *

from analytics import *

from charts import *


while True:

    print("""
===== EXPENSE TRACKER =====

1. Add Expense
2. View Expenses
3. Search Expense
4. Delete Expense
5. Update Expense
6. Show Statistics
7. Category Statistics
8. Category Pie Chart
9. Category Bar Chart
10. Monthly Expense Analysis
11. Exit
""")
    
    choice = input("Enter Choice: ")


    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        search_menu()

    elif choice == "4":
        delete_expense()

    elif choice == "5":
        update_expense()

    elif choice == "6":
        show_statistics()

    elif choice == "7":
        category_statistics()

    elif choice == "8":
        category_pie_chart()

    elif choice == "9":
        category_bar_chart()

    elif choice == "10":
        monthly_expense_analysis()

    elif choice == "11":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice")

conn.close()