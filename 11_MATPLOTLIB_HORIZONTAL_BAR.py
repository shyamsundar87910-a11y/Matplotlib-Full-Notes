```python
# ===================== 11_MATPLOTLIB_HORIZONTAL_BAR.py =====================


import matplotlib.pyplot as plt


# .........................Simple Horizontal Bar Chart.........................#

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

plt.barh(
    products,
    sales
)

plt.title("Product Sales")

plt.xlabel("Sales")

plt.ylabel("Products")

plt.show()


# .........................Horizontal Bar with Color.........................#

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

plt.barh(
    products,
    sales,
    color="skyblue"
)

plt.title("Product Sales")

plt.xlabel("Sales")

plt.ylabel("Products")

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

plt.barh(
    products,
    sales,
    color=colors
)

plt.title("Product Sales")

plt.xlabel("Sales")

plt.ylabel("Products")

plt.show()


# .........................Bar Height.........................#

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

plt.barh(
    products,
    sales,
    height=0.5
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

plt.barh(
    products,
    sales,
    color="lightgreen",
    edgecolor="black"
)

plt.title("Product Sales")

plt.show()


# .........................Horizontal Bar with Grid.........................#

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

plt.barh(
    products,
    sales,
    color="steelblue"
)

plt.title("Product Sales")

plt.xlabel("Sales")

plt.ylabel("Products")

plt.grid(
    axis="x",
    linestyle="--",
    alpha=0.6
)

plt.show()


# .........................Horizontal Bar with Values.........................#

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

plt.barh(
    products,
    sales,
    color="orange"
)

for i in range(len(products)):
    plt.text(
        sales[i],
        i,
        sales[i],
        va="center"
    )

plt.title("Product Sales")

plt.xlabel("Sales")

plt.ylabel("Products")

plt.show()


# .........................Monthly Sales Example.........................#

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

plt.barh(
    months,
    sales,
    color="green"
)

plt.title("Monthly Sales")

plt.xlabel("Sales")

plt.ylabel("Month")

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

plt.barh(
    students,
    marks,
    color="purple"
)

plt.title("Student Marks")

plt.xlabel("Marks")

plt.ylabel("Students")

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

plt.barh(
    departments,
    employees,
    color="teal"
)

plt.title("Employees by Department")

plt.xlabel("Employees")

plt.ylabel("Department")

plt.show()


# .........................Sorted Horizontal Bar Chart.........................#

products = [
    "Monitor",
    "Tablet",
    "Mobile",
    "Laptop"
]

sales = [
    15
```
