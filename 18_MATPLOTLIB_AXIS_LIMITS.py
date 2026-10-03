```python
# ===================== 18_MATPLOTLIB_AXIS_LIMITS.py =====================


import matplotlib.pyplot as plt


# .........................Basic Axis Limits.........................#

x = [1, 2, 3, 4, 5]

y = [10, 20, 15, 30, 25]

plt.plot(
    x,
    y
)

plt.title("Basic Axis Limits")

plt.show()


# .........................X-Axis Limit.........................#

x = [1, 2, 3, 4, 5, 6]

y = [10, 20, 15, 30, 25, 35]

plt.plot(
    x,
    y
)

plt.xlim(
    1,
    5
)

plt.title("X-Axis Limit")

plt.show()


# .........................Y-Axis Limit.........................#

x = [1, 2, 3, 4, 5]

y = [10, 20, 15, 30, 25]

plt.plot(
    x,
    y
)

plt.ylim(
    0,
    30
)

plt.title("Y-Axis Limit")

plt.show()


# .........................Both X and Y Limits.........................#

x = [1, 2, 3, 4, 5, 6]

y = [10, 20, 15, 30, 25, 35]

plt.plot(
    x,
    y
)

plt.xlim(
    1,
    5
)

plt.ylim(
    0,
    30
)

plt.title("X and Y Axis Limits")

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
    45,
    60,
    75,
    85,
    95
]

plt.plot(
    students,
    marks,
    marker="o"
)

plt.ylim(
    0,
    100
)

plt.title("Student Marks")

plt.xlabel("Students")

plt.ylabel("Marks")

plt.show()


# .........................Sales Example.........................#

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

plt.plot(
    months,
    sales,
    marker="o"
)

plt.ylim(
    0,
    45000
)

plt.title("Monthly Sales")

plt.xlabel("Month")

plt.ylabel("Sales")

plt.grid()

plt.show()


# .........................Bar Chart with Axis Limits.........................#

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
    sales
)

plt.ylim(
    0,
    60000
)

plt.title("Product Sales")

plt.xlabel("Products")

plt.ylabel("Sales")

plt.show()


# .........................Scatter Plot with Axis Limits.........................#

hours = [
    1,
    2,
    3,
    4,
    5,
    6,
    7
]

marks = [
    40,
    45,
    55,
    65,
    72,
    82
```
