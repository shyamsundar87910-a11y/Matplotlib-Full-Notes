```python
# ===================== 06_MATPLOTLIB_LABELS.py =====================


import matplotlib.pyplot as plt


# .........................Simple Title.........................#

x = [1, 2, 3, 4, 5]

y = [10, 20, 15, 30, 25]

plt.plot(
    x,
    y
)

plt.title("Simple Line Chart")

plt.show()


# .........................X-axis Label.........................#

x = [1, 2, 3, 4, 5]

y = [20, 30, 25, 40, 35]

plt.plot(
    x,
    y
)

plt.xlabel("Days")

plt.show()


# .........................Y-axis Label.........................#

x = [1, 2, 3, 4, 5]

y = [15, 25, 20, 35, 30]

plt.plot(
    x,
    y
)

plt.ylabel("Sales")

plt.show()


# .........................Title and Both Labels.........................#

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

plt.plot(
    months,
    sales
)

plt.title("Monthly Sales")

plt.xlabel("Month")

plt.ylabel("Sales")

plt.show()


# .........................Title with Font Size.........................#

x = [1, 2, 3, 4, 5]

y = [10, 25, 20, 35, 40]

plt.plot(
    x,
    y
)

plt.title(
    "Sales Growth",
    fontsize=16
)

plt.show()


# .........................X-axis Label with Font Size.........................#

x = [1, 2, 3, 4, 5]

y = [20, 30, 25, 40, 50]

plt.plot(
    x,
    y
)

plt.xlabel(
    "Month",
    fontsize=12
)

plt.show()


# .........................Y-axis Label with Font Size.........................#

x = [1, 2, 3, 4, 5]

y = [15, 25, 35, 30, 45]

plt.plot(
    x,
    y
)

plt.ylabel(
    "Sales Amount",
    fontsize=12
)

plt.show()


# .........................Title and Labels with Figure Size.........................#

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

plt.figure(
    figsize=(8, 5)
)

plt.plot(
    months,
    sales,
    marker="o"
)

plt.title(
    "Monthly Sales Analysis",
    fontsize=16
)

plt.xlabel(
    "Month",
    fontsize=12
)

plt.ylabel(
    "Sales",
    fontsize=12
)

plt.show()


# .........................Title Padding.........................#

x = [1, 2, 3, 4, 5]

y = [10, 20, 30, 25, 40]

plt.plot(
    x,
    y
)

plt.title(
    "Sales Chart",
    pad=20
)

plt.xlabel("Month")

plt.ylabel("Sales")

plt.show()


# .........................X-axis Label Padding.........................#

x = [1, 2, 3, 4, 5]

y = [20, 25, 30, 35, 40]

plt.plot(
    x,
    y
)

plt.xlabel(
    "Month",
    labelpad=10
)

plt.ylabel("Sales")

plt.title("Label Padding")

plt.show()


# .........................Y-axis Label Padding.........................#

x = [1, 2, 3, 4, 5]

y = [15, 30, 25, 40, 35]

plt.plot(
    x,
    y
)

plt.xlabel("Month")

plt.ylabe
```
