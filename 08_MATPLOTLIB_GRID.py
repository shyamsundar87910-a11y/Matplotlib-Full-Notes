```python
# ===================== 08_MATPLOTLIB_GRID.py =====================


import matplotlib.pyplot as plt


# .........................Simple Grid.........................#

x = [1, 2, 3, 4, 5]

y = [10, 20, 15, 30, 25]

plt.plot(
    x,
    y
)

plt.title("Simple Grid")

plt.grid()

plt.show()


# .........................Grid with Line Plot.........................#

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
    28000,
    35000
]

plt.plot(
    months,
    sales,
    marker="o"
)

plt.title("Monthly Sales")

plt.xlabel("Month")

plt.ylabel("Sales")

plt.grid()

plt.show()


# .........................Turn Grid Off.........................#

x = [1, 2, 3, 4, 5]

y = [10, 20, 15, 30, 25]

plt.plot(
    x,
    y
)

plt.grid(False)

plt.show()


# .........................X-Axis Grid.........................#

x = [1, 2, 3, 4, 5]

y = [20, 35, 25, 40, 30]

plt.plot(
    x,
    y,
    marker="o"
)

plt.title("X-Axis Grid")

plt.grid(
    axis="x"
)

plt.show()


# .........................Y-Axis Grid.........................#

x = [1, 2, 3, 4, 5]

y = [20, 35, 25, 40, 30]

plt.plot(
    x,
    y,
    marker="o"
)

plt.title("Y-Axis Grid")

plt.grid(
    axis="y"
)

plt.show()


# .........................Custom Grid Line Style.........................#

x = [1, 2, 3, 4, 5]

y = [10, 25, 20, 35, 30]

plt.plot(
    x,
    y
)

plt.grid(
    linestyle="--"
)

plt.title("Dashed Grid")

plt.show()


# .........................Dotted Grid.........................#

x = [1, 2, 3, 4, 5]

y = [15, 30, 20, 40, 35]

plt.plot(
    x,
    y
)

plt.grid(
    linestyle=":"
)

plt.title("Dotted Grid")

plt.show()


# .........................Grid Line Width.........................#

x = [1, 2, 3, 4, 5]

y = [10, 20, 30, 25, 40]

plt.plot(
    x,
    y
)

plt.grid(
    linewidth=2
)

plt.title("Grid Line Width")

plt.show()


# .........................Grid with Transparency.........................#

x = [1, 2, 3, 4, 5]

y = [20, 30, 25, 40, 35]

plt.plot(
    x,
    y,
    marker="o"
)

plt.grid(
    alpha=0.5
)

plt.title("Grid with Transparency")

plt.show()


# .........................Grid with Multiple Customizations.........................#

x = [1, 2, 3, 4, 5]

y = [15, 25, 20, 35, 30]

plt.plot(
    x,
    y,
    marker="o"
)

plt.grid(
    linestyle="--",
    linewidth=1,
    alpha=0.7
)

plt.title("Customized Grid")

plt.show()


# .........................Bar Chart with Grid.........................#

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

plt.title("Product Sales")

plt.xlabel("Product")

plt.ylabel("Sales")

plt.grid(
    axis="y"
)

plt.show()


# .........................Scatter Plot with Grid.........................#

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
    marks
)

plt.title("Study Hours and Marks")

plt.xlabel("Study Hours")

plt.ylabel("Marks")

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

plt.plot(
    students,
    marks,
    marker="o"
)

plt.title("Student Marks")

plt.xlabel("Students")

plt.ylabel("Marks")

plt.grid(
    axis="y",
    linestyle="--"
)

plt.show()


# .........................Sales and Expenses Example.........................#

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

plt.
```
