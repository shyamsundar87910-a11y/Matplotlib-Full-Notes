```python
# ===================== 02_MATPLOTLIB_FIGURE.py =====================


import matplotlib.pyplot as plt


# .........................Basic Figure.........................#

x = [1, 2, 3, 4, 5]

y = [10, 20, 15, 30, 25]

plt.figure()

plt.plot(x, y)

plt.title("Basic Figure")

plt.show()


# .........................Figure Size.........................#

x = [1, 2, 3, 4, 5]

y = [20, 30, 25, 40, 35]

plt.figure(
    figsize=(8, 5)
)

plt.plot(x, y)

plt.title("Figure with Size")

plt.xlabel("X Values")

plt.ylabel("Y Values")

plt.show()


# .........................Small Figure.........................#

x = [1, 2, 3, 4, 5]

y = [10, 15, 20, 25, 30]

plt.figure(
    figsize=(5, 3)
)

plt.plot(x, y)

plt.title("Small Figure")

plt.show()


# .........................Large Figure.........................#

x = [1, 2, 3, 4, 5]

y = [15, 25, 20, 35, 40]

plt.figure(
    figsize=(10, 6)
)

plt.plot(x, y)

plt.title("Large Figure")

plt.show()


# .........................Figure with Line Plot.........................#

months = [
    "January",
    "February",
    "March",
    "April",
    "May"
]

sales = [
    20000,
    25000,
    30000,
    28000,
    35000
]

plt.figure(
    figsize=(8, 5)
)

plt.plot(
    months,
    sales
)

plt.title("Monthly Sales")

plt.xlabel("Month")

plt.ylabel("Sales")

plt.show()


# .........................Figure with Bar Chart.........................#

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

plt.figure(
    figsize=(8, 5)
)

plt.bar(
    products,
    sales
)

plt.title("Product Sales")

plt.xlabel("Product")

plt.ylabel("Sales")

plt.show()


# .........................Multiple Figures.........................#

x = [1, 2, 3, 4, 5]

sales = [10, 20, 30, 25, 40]

marks = [50, 60, 70, 80, 90]


plt.figure(
    figsize=(7, 4)
)

plt.plot(
    x,
    sales
)

plt.title("Sales Chart")

plt.show()


plt.figure(
    figsize=(7, 4)
)

plt.plot(
    x,
    marks
)

plt.title("Marks Chart")

plt.show()


# .........................Figure Number.........................#

plt.figure(
    num=1,
    figsize=(7, 4)
)

x = [1, 2, 3, 4, 5]

y = [10, 20, 30, 40, 50]

plt.plot(x, y)

plt.title("Figure Number 1")

plt.show()


plt.figure(
    num=2,
    figsize=(7, 4)
)

y = [50, 40, 30, 20, 10]

plt.plot(x, y)

plt.title("Figure Number 2")

plt.show()


# .........................Figure with Multiple Lines.........................#

months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May"
]

sales_2025 = [
    20000,
    25000,
    30000,
    28000,
    35000
]

sales_2026 = [
    25000,
    28000,
    32000,
    35000,
    40000
]

plt.figure(
    figsize=(9, 5)
)

plt.plot(
    months,
    sales_2025
)

plt.plot(
    months,
    sales_2026
)

plt.title("Sales Comparison")

plt.xlabel("Month")

plt.ylabel("Sales")

plt.show()


# .........................Figure with Grid.........................#

x = [1, 2, 3, 4, 5]

y = [15, 25, 20, 35, 30]

plt.figure(
    figsize=(8, 5)
)

plt.plot(
    x,
    y
)

plt.title("Figure with Grid")

plt.xlabel("X Values")

plt.ylabel("Y Values")

plt.grid()

plt.show()


# .........................Figure Functions.........................#

# plt.figure()      -> Creates a new figure
# figsize           -> Sets figure width and height
# num               -> Gives a figure number
# plt.show()        -> Displays the figure
# plt.grid()        -> Adds grid lines


# .........................Important Note.........................#

# figsize=(width, height)
#
# Example:
# figsize=(8, 5)
#
# 8 -> Figure width
# 5 -> Figure height
```
