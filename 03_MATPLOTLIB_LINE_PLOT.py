```python
# ===================== 03_MATPLOTLIB_LINE_PLOT.py =====================


import matplotlib.pyplot as plt


# .........................Simple Line Plot.........................#

x = [1, 2, 3, 4, 5]

y = [10, 20, 15, 30, 25]

plt.plot(
    x,
    y
)

plt.show()


# .........................Line Plot with Title.........................#

x = [1, 2, 3, 4, 5]

y = [20, 30, 25, 40, 35]

plt.plot(
    x,
    y
)

plt.title("Simple Line Plot")

plt.show()


# .........................Line Plot with Labels.........................#

x = [1, 2, 3, 4, 5]

y = [15, 25, 20, 35, 30]

plt.plot(
    x,
    y
)

plt.title("Sales Data")

plt.xlabel("Month")

plt.ylabel("Sales")

plt.show()


# .........................Line Plot with Custom X Values.........................#

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
    22000,
    30000,
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


# .........................Line Plot with Marker.........................#

x = [1, 2, 3, 4, 5]

y = [10, 25, 20, 35, 40]

plt.plot(
    x,
    y,
    marker="o"
)

plt.title("Line Plot with Marker")

plt.xlabel("X Values")

plt.ylabel("Y Values")

plt.show()


# .........................Multiple Lines.........................#

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


# .........................Three Lines.........................#

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
    sales
)

plt.plot(
    months,
    expenses
)

plt.plot(
    months,
    profit
)

plt.title("Sales, Expenses and Profit")

plt.xlabel("Month")

plt.ylabel("Amount")

plt.show()


# .........................Line Plot with Figure Size.........................#

x = [1, 2, 3, 4, 5]

y = [10, 20, 30, 25, 40]

plt.figure(
    figsize=(8, 5)
)

plt.plot(
    x,
    y
)

plt.title("Line Plot with Figure Size")

plt.xlabel("X Values")

plt.ylabel("Y Values")

plt.show()


# .........................Line Plot with Grid.........................#

x = [1, 2, 3, 4, 5]

y = [15, 30, 20, 35, 40]

plt.plot(
    x,
    y
)

plt.title("Line Plot with Grid")

plt.xlabel("X Values")

plt.ylabel("Y Values")

plt.grid()

plt.show()


# .........................Student Marks Trend.........................#

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
    85,
    78,
    90
]

plt.plot(
    students,
    marks,
    marker="o"
)

plt.title("Student Marks")

plt.xlabel("Students")

plt.ylabel("Marks")

plt.grid()

plt.show()


# .........................Temperature Trend.........................#

days = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday"
]

temperature = [
    28,
    30,
    29,
    32,
    31
]

plt.plot(
    days,
    temperature,
    marker="o"
)

plt.title("Weekly Temperature")

plt.xlabel("Day")

plt.ylabel("Temperature")

plt.grid()

plt.show()


# .........................Increasing Data.........................#

x = [1, 2, 3, 4, 5]

y = [10, 20, 30, 40, 50]

plt.plot(
    x,
    y
)

plt.title("Increasing Data")

plt.show()


# .........................Decreasing Data.........................#

x = [1, 2, 3, 4, 5]

y = [50, 40, 30, 20, 10]

plt.plot(
    x,
    y
)

plt.title("Decreasing Data")

plt.show()


# .........................Line Plot Functions.........................#

# plt.plot()       -> Creates a line plot
# plt.title()      -> Adds title
# plt.xlabel()     -> Adds X-axis label
# plt.ylabel()     -> Adds Y-axis label
# plt.grid()       -> Adds grid
# plt.figure()     -> Creates a new figure
# plt.show()       -> Displays the plot


# .........................Important Syntax.........................#

# plt.plot(x, y)
#
# x -> X-axis values
# y -> Y-axis values
#
# Example:
#
# plt.plot(
#     [1, 2, 3],
#     [10, 20, 30]
# )
```
