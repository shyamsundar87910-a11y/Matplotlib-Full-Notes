```python id="d1m5yq"
# ===================== 20_MATPLOTLIB_TEXT.py =====================


import matplotlib.pyplot as plt


# .........................Basic Text.........................#

x = [1, 2, 3, 4, 5]

y = [10, 20, 15, 30, 25]

plt.plot(
    x,
    y,
    marker="o"
)

plt.text(
    3,
    15,
    "Important Point"
)

plt.title("Basic Text")

plt.show()


# .........................Text with Position.........................#

x = [1, 2, 3, 4, 5]

y = [10, 20, 15, 30, 25]

plt.plot(
    x,
    y,
    marker="o"
)

plt.text(
    2,
    20,
    "Value = 20"
)

plt.text(
    4,
    30,
    "Highest Value"
)

plt.title("Text Position")

plt.show()


# .........................Text on Bar Chart.........................#

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

plt.text(
    0,
    50000,
    "50000"
)

plt.text(
    1,
    35000,
    "35000"
)

plt.text(
    2,
    20000,
    "20000"
)

plt.text(
    3,
    15000,
    "15000"
)

plt.title("Product Sales")

plt.xlabel("Products")

plt.ylabel("Sales")

plt.show()


# .........................Text with Alignment.........................#

x = [1, 2, 3, 4, 5]

y = [10, 20, 15, 30, 25]

plt.plot(
    x,
    y,
    marker="o"
)

plt.text(
    3,
    15,
    "Center Text",
    ha="center",
    va="bottom"
)

plt.title("Text Alignment")

plt.show()


# .........................Text with Font Size.........................#

x = [1, 2, 3, 4, 5]

y = [10, 20, 15, 30, 25]

plt.plot(
    x,
    y,
    marker="o"
)

plt.text(
    3,
    15,
    "Important",
    fontsize=14
)

plt.title("Text Font Size")

plt.show()


# .........................Text with Rotation.........................#

x = [1, 2, 3, 4, 5]

y = [10, 20, 15, 30, 25]

plt.plot(
    x,
    y,
    marker="o"
)

plt.text(
    3,
    15,
    "Rotated Text",
    rotation=45
)

plt.title("Text Rotation")

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
    marks
)

for i in range(len(students)):
    plt.text(
        i,
        marks[i],
        str(marks[i]),
        ha="center",
        va="bottom"
    )

plt.ylim(
    0,
    100
)

plt.title("Student Marks")

plt.xlabel("Students")

plt.ylabel("Marks")

plt.show()


# .........................Sales Values Example.........................#

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

plt.bar(
    months,
    sales
)

for i in range(len(months)):
    plt.text(
        i,
        sales[i],
        str(sales[i]),
        ha="center",
        va="bottom"
    )

plt.title("Monthly Sales")

plt.xlabel("Month")

plt.ylabel("Sales")

plt.show()


# .........................Scatter Plot Text.........................#

hours = [
    1,
    2,
    3,
    4,
    5
]

marks = [
    45,
    50,
    60,
    75,
    85
]

plt.scatte
```
