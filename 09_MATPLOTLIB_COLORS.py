```python
# ===================== 09_MATPLOTLIB_COLORS.py =====================


import matplotlib.pyplot as plt


# .........................Simple Color.........................#

x = [1, 2, 3, 4, 5]

y = [10, 20, 15, 30, 25]

plt.plot(
    x,
    y,
    color="red"
)

plt.title("Red Line")

plt.show()


# .........................Different Line Colors.........................#

x = [1, 2, 3, 4, 5]

sales = [20, 30, 25, 40, 35]

expenses = [15, 20, 18, 25, 22]

plt.plot(
    x,
    sales,
    color="blue",
    label="Sales"
)

plt.plot(
    x,
    expenses,
    color="green",
    label="Expenses"
)

plt.title("Sales and Expenses")

plt.legend()

plt.show()


# .........................Common Colors.........................#

x = [1, 2, 3, 4, 5]

y = [10, 20, 15, 30, 25]

plt.plot(
    x,
    y,
    color="blue"
)

plt.show()


# .........................Short Color Codes.........................#

x = [1, 2, 3, 4, 5]

y = [15, 25, 20, 35, 30]

plt.plot(
    x,
    y,
    color="r"
)

plt.show()


# .........................Green Short Code.........................#

x = [1, 2, 3, 4, 5]

y = [10, 25, 20, 35, 30]

plt.plot(
    x,
    y,
    color="g"
)

plt.show()


# .........................Blue Short Code.........................#

x = [1, 2, 3, 4, 5]

y = [20, 30, 25, 40, 35]

plt.plot(
    x,
    y,
    color="b"
)

plt.show()


# .........................Marker Color.........................#

x = [1, 2, 3, 4, 5]

y = [10, 20, 15, 30, 25]

plt.plot(
    x,
    y,
    marker="o",
    markerfacecolor="yellow"
)

plt.title("Marker Color")

plt.show()


# .........................Line Color and Marker Color.........................#

x = [1, 2, 3, 4, 5]

y = [20, 30, 25, 40, 35]

plt.plot(
    x,
    y,
    color="blue",
    marker="o",
    markerfacecolor="yellow"
)

plt.title("Line and Marker Colors")

plt.show()


# .........................Marker Edge Color.........................#

x = [1, 2, 3, 4, 5]

y = [15, 25, 20, 35, 30]

plt.plot(
    x,
    y,
    marker="o",
    markerfacecolor="yellow",
    markeredgecolor="red"
)

plt.title("Marker Edge Color")

plt.show()


# .........................Bar Chart Colors.........................#

products = [
    "Laptop",
    "Mobile",
    "Tablet",
    "Monitor"
]

sales = [
    50000,
    35000,
    20000,
    15000
]

plt.bar(
    products,
    sales,
    color="skyblue"
)

plt.title("Product Sales")

plt.xlabel("Product")

plt.ylabel("Sales")

plt.show()


# .........................Different Bar Colors.........................#

products = [
    "Laptop",
    "Mobile",
    "Tablet",
    "Monitor"
]

sales = [
    50000,
    35000,
    20000,
    15000
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

plt.show()


# .........................Scatter Plot Color.........................#

hours = [
    1,
    2,
    3,
    4,
    5,
    6
]

marks = [
    45,
    50,
    60,
    65,
    75,
    85
]

plt.scatter(
    hours,
    marks,
    color="purple"
)

plt.title("Study Hours and Marks")

plt.xlabel("Study Hours")

plt.ylabel("Marks")

plt.show()


# .........................Histogram Color.........................#

marks = [
    45,
    50,
    55,
    60,
    65,
    70,
    72,
    75,
    80,
    85,
    90,
    95
]

plt.hist(
    marks,
    color="orange"
)

plt.title("Marks Distribution")

plt.xlabel("Marks")

plt.ylabel("Students")

plt.show()


# .........................Pie Chart Colors.........................#

products = [
    "Laptop",
    "Mobile",
    "Tablet",
    "Monitor"
]

sales = [
    40,
    30,
    20,
    10
]

colors = [
    "red",
    "blue",
    "green",
    "orange"
]

plt.pie(
    sales,
    labels=products,
    colors=colors,
    autopct="%1.1f%%"
)

plt.title("Product Sales Distribution")

plt.show()


# .........................Color with Transparency.........................#

x = [1, 2, 3, 4, 5]

y = [10, 20, 15, 30, 25]

plt.plot(
    x,
    y,
    color="blue",
    alpha=0.5
)

plt.title("Transparent Line")

plt.show()


# .........................Multiple Colored Lines.........................#

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

profit = [
    5000,
    7000,
    8000,
    10000,
    12000
]

plt.plot(
    months,
    sales,
    color="blue",
    label="Sales"
)

plt.plot(
    months,
    expenses,
    color="red",
    label="Expenses"
)

plt.plot(
    months,
    profit,
    color="green",
    label="Profit"
)

plt.title("Business Analysis")

plt.xlabel("Month")

plt.ylabel("Amount")

plt.legend()

plt.grid()

plt.show()


# .........................Student Performance Example.........................#

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
    color="steelblue"
)

plt.title("Student Marks")

plt.xlabel("Students")

plt.ylabel("Marks")

plt.show()


# .........................Important Color Parameters.........................#

# color
#       -> Changes line or chart color
#
# markerfacecolor
#       -> Changes marker insid
```
