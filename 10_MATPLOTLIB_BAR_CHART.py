```python
# ===================== 10_MATPLOTLIB_BAR_CHART.py =====================


import matplotlib.pyplot as plt


# .........................Simple Bar Chart.........................#

products = [
    "Laptop",
    "Mobile",
    "Tablet",
    "Monitor"
]

sales = [
    50,
    35,
    20,
    15
]

plt.bar(
    products,
    sales
)

plt.title("Product Sales")

plt.xlabel("Products")

plt.ylabel("Sales")

plt.show()


# .........................Bar Chart with Color.........................#

products = [
    "Laptop",
    "Mobile",
    "Tablet",
    "Monitor"
]

sales = [
    50,
    35,
    20,
    15
]

plt.bar(
    products,
    sales,
    color="skyblue"
)

plt.title("Product Sales")

plt.show()


# .........................Different Bar Colors.........................#

products = [
    "Laptop",
    "Mobile",
    "Tablet",
    "Monitor"
]

sales = [
    50,
    35,
    20,
    15
]

colors = [
    "red",
    "blue",
    "green",
    "orange"
]

plt.bar(
    products,
    sales,
    color=colors
)

plt.title("Product Sales")

plt.xlabel("Products")

plt.ylabel("Sales")

plt.show()


# .........................Bar Width.........................#

products = [
    "Laptop",
    "Mobile",
    "Tablet",
    "Monitor"
]

sales = [
    50,
    35,
    20,
    15
]

plt.bar(
    products,
    sales,
    width=0.5
)

plt.title("Product Sales")

plt.show()


# .........................Bar Edge Color.........................#

products = [
    "Laptop",
    "Mobile",
    "Tablet",
    "Monitor"
]

sales = [
    50,
    35,
    20,
    15
]

plt.bar(
    products,
    sales,
    color="lightblue",
    edgecolor="black"
)

plt.title("Product Sales")

plt.show()


# .........................Bar Line Width.........................#

products = [
    "Laptop",
    "Mobile",
    "Tablet",
    "Monitor"
]

sales = [
    50,
    35,
    20,
    15
]

plt.bar(
    products,
    sales,
    edgecolor="black",
    linewidth=2
)

plt.title("Product Sales")

plt.show()


# .........................Bar Chart with Grid.........................#

products = [
    "Laptop",
    "Mobile",
    "Tablet",
    "Monitor"
]

sales = [
    50,
    35,
    20,
    15
]

plt.bar(
    products,
    sales,
    color="steelblue"
)

plt.title("Product Sales")

plt.xlabel("Products")

plt.ylabel("Sales")

plt.grid(
    axis="y",
    linestyle="--",
    alpha=0.6
)

plt.show()


# .........................Bar Chart with Values.........................#

products = [
    "Laptop",
    "Mobile",
    "Tablet",
    "Monitor"
]

sales = [
    50,
    35,
    20,
    15
]

plt.bar(
    products,
    sales
)

for i in range(len(products)):
    plt.text(
        i,
        sales[i],
        sales[i],
        ha="center"
    )

plt.title("Product Sales")

plt.xlabel("Products")

plt.ylabel("Sales")

plt.show()


# .........................Monthly Sales Example.........................#

months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun"
]

sales = [
    20000,
    25000,
    30000,
    28000,
    35000,
    40000
]

plt.bar(
    months,
    sales,
    color="green"
)

plt.title("Monthly Sales")

plt.xlabel("Month")

plt.ylabel("Sales")

plt.show()


# .........................Student Marks Example.........................#

students = [
    "Aman",
    "Rahul",
    "Priya",
    "Sneha",
    "Rohit"
]

marks = [
    65,
    72,
    88,
    78,
    92
]

plt.bar(
    students,
    marks,
    color="orange"
)

plt.title("Student Marks")

plt.xlabel("Students")

plt.ylabel("Marks")

plt.show()


# .........................Department Employees Example.........................#

departments = [
    "IT",
    "HR",
    "Sales",
    "Finance"
]

employees = [
    25,
    15,
    30,
    20
]

plt.bar(
    departments,
    employees,
    color="purple"
)

plt.title("Employees by Department")

plt.xlabel("Department")

plt.ylabel("Number of Employees")

plt.show()


# .........................Sales and Expenses Bar Chart.........................#

months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May"
]

sales = [
    20000,
    25000,
    30000,
    35000,
    40000
]

expenses = [
    15000,
    18000,
    22000,
    25000,
    28000
]

x = range(len(months))

plt.bar(
    x,
    sales,
    width=0.4,
    label="Sales"
)

plt.bar(
    [i + 0.4 for i in x],
    expenses,
    width=0.4,
    label="Expenses"
)

plt.xticks(
    [i + 0.2 for i in x],
    months
)

plt.title("Sales and Expenses")

plt.xlabel("Month")

plt.ylabel("Amount")

plt.legend()

plt.show()


# .........................Horizontal Comparison Using Bar.........................#

products = [
    "Laptop",
    "Mobile",
    "Tablet",
    "Monitor"
]

sales = [
    50,
    35,
    20,
    15
]

plt.bar(
    products,
    sales,
    color="teal"
)

plt.title("Product Sales Comparison")

plt.xlabel("Products")

plt.ylabel("Sales")

plt.grid(
    ax
```
