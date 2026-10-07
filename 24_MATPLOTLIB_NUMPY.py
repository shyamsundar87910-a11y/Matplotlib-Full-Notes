```python id="r4n6kc"
# ===================== 24_MATPLOTLIB_NUMPY.py =====================


import numpy as np

import matplotlib.pyplot as plt


# .........................NumPy Array with Line Plot.........................#

x = np.array(
    [1, 2, 3, 4, 5]
)

y = np.array(
    [10, 20, 15, 30, 25]
)

plt.plot(
    x,
    y,
    marker="o"
)

plt.title("NumPy Array Line Plot")

plt.xlabel("X Values")

plt.ylabel("Y Values")

plt.show()


# .........................NumPy arange().........................#

x = np.arange(
    1,
    11
)

y = x * 2

plt.plot(
    x,
    y,
    marker="o"
)

plt.title("NumPy arange with Matplotlib")

plt.xlabel("X Values")

plt.ylabel("Y Values")

plt.grid()

plt.show()


# .........................NumPy linspace().........................#

x = np.linspace(
    0,
    10,
    100
)

y = x ** 2

plt.plot(
    x,
    y
)

plt.title("NumPy linspace")

plt.xlabel("X Values")

plt.ylabel("Y Values")

plt.show()


# .........................NumPy Mathematical Calculation.........................#

x = np.arange(
    1,
    11
)

y = x ** 2

plt.plot(
    x,
    y,
    marker="o"
)

plt.title("Square of Numbers")

plt.xlabel("Number")

plt.ylabel("Square")

plt.show()


# .........................Multiple NumPy Arrays.........................#

months = np.array(
    [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May"
    ]
)

sales = np.array(
    [
        20000,
        25000,
        30000,
        35000,
        40000
    ]
)

expenses = np.array(
    [
        15000,
        18000,
        22000,
        25000,
        28000
    ]
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
    marker="s",
    label="Expenses"
)

plt.title("Sales and Expenses")

plt.xlabel("Month")

plt.ylabel("Amount")

plt.legend()

plt.grid()

plt.show()


# .........................NumPy Bar Chart.........................#

products = np.array(
    [
        "Laptop",
        "Mobile",
        "Tablet",
        "Monitor"
    ]
)

sales = np.array(
    [
        50000,
        35000,
        20000,
        15000
    ]
)

plt.bar(
    products,
    sales
)

plt.title("Product Sales")

plt.xlabel("Products")

plt.ylabel("Sales")

plt.show()


# .........................NumPy Scatter Plot.........................#

hours = np.array(
    [
        1,
        2,
        3,
        4,
        5,
        6
    ]
)

marks = np.array(
    [
        45,
        50,
        60,
        65,
        75,
        85
    ]
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


# .........................NumPy Histogram.........................#

marks = np.array(
    [
        45,
        50,
        55,
        60,
        65,
        70,
        75,
        80,
        85,
        90,
        95
    ]
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


# .........................NumPy Pie Chart.........................#

subjects = np.array(
    [
        "Python",
        "SQL",
        "Excel",
        "Power BI"
    ]
)

study_hours = np.array(
    [
        30,
        25,
        20,
        25
    ]
)

plt.pie(
    study_hour_
```
