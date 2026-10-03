```python
# ===================== 17_MATPLOTLIB_FIGURE_SIZE.py =====================


import matplotlib.pyplot as plt


# .........................Default Figure Size.........................#

x = [1, 2, 3, 4, 5]

y = [10, 20, 15, 30, 25]

plt.plot(
    x,
    y
)

plt.title("Default Figure")

plt.show()


# .........................Small Figure.........................#

x = [1, 2, 3, 4, 5]

y = [10, 20, 15, 30, 25]

plt.figure(
    figsize=(5, 3)
)

plt.plot(
    x,
    y
)

plt.title("Small Figure")

plt.show()


# .........................Large Figure.........................#

x = [1, 2, 3, 4, 5]

y = [10, 20, 15, 30, 25]

plt.figure(
    figsize=(10, 6)
)

plt.plot(
    x,
    y
)

plt.title("Large Figure")

plt.show()


# .........................Wide Figure.........................#

x = [1, 2, 3, 4, 5]

y = [10, 20, 15, 30, 25]

plt.figure(
    figsize=(12, 4)
)

plt.plot(
    x,
    y
)

plt.title("Wide Figure")

plt.show()


# .........................Square Figure.........................#

x = [1, 2, 3, 4, 5]

y = [10, 20, 15, 30, 25]

plt.figure(
    figsize=(6, 6)
)

plt.plot(
    x,
    y
)

plt.title("Square Figure")

plt.show()


# .........................Bar Chart with Figure Size.........................#

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

plt.xlabel("Products")

plt.ylabel("Sales")

plt.show()


# .........................Pie Chart with Figure Size.........................#

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

plt.figure(
    figsize=(7, 7)
)

plt.pie(
    sales,
    labels=products,
    autopct="%1.1f%%"
)

plt.title("Product Sales Distribution")

plt.show()


# .........................Scatter Plot with Figure Size.........................#

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

plt.figure(
    figsize=(9, 5)
)

plt.scatter(
    hours,
    marks,
    s=100
)

plt.title("Study Hours and Marks")

plt.xlabel("Study Hours")

plt.ylabel("Marks")

plt.grid()

plt.show()


# .........................Histogram with Figure Size.........................#

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

plt.figure(
    figsize=(8, 5)
)

plt.hist(
    marks,
    bins=5,
    edgecolor="black"
)

plt.title("Marks Distribution")

plt.xlabel("Marks")

plt.ylabel("Students")

plt.show()


# .........................Box Plot with Figure Size.........................#

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

plt.figure(
    figsize=(6, 5)
)

plt.boxplot(
    marks
)

plt.title("Marks Distribution")

plt.ylabel("Marks")

plt.show()


# .........................Multiple Plots with Figure Size.........................#

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

plt.figure(
    figsize=(10, 6)
)

plt.plot(
    months,
    sales,
    marker="o",
    label="Sales"
)

plt.plot(
    months,
    expenses,
    marker="o",
    label="Expenses"
)

plt.title("Sales and Expenses")

plt.xlabel("Month")

plt.ylabel("Amount")

plt.legend()

plt.grid()

plt.show()


# .........................Subplots with Figure Size.........................#

plt.figure(
    figsize=(10, 6)
)


plt.subplot(
    2,
    2,
    1
)

plt.plot(
    [1, 2, 3, 4],
    [10, 20, 15, 30]
)

plt.title("Line Plo
```
