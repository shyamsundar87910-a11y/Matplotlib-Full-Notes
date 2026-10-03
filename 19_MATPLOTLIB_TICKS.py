```python
# ===================== 19_MATPLOTLIB_TICKS.py =====================


import matplotlib.pyplot as plt


# .........................Basic Ticks.........................#

x = [1, 2, 3, 4, 5]

y = [10, 20, 15, 30, 25]

plt.plot(
    x,
    y,
    marker="o"
)

plt.xticks(
    [1, 2, 3, 4, 5]
)

plt.yticks(
    [0, 10, 20, 30, 40]
)

plt.title("Basic Ticks")

plt.show()


# .........................Custom X-Axis Ticks.........................#

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

plt.plot(
    months,
    sales,
    marker="o"
)

plt.xticks(
    months
)

plt.title("Monthly Sales")

plt.xlabel("Month")

plt.ylabel("Sales")

plt.show()


# .........................Custom Y-Axis Ticks.........................#

x = [1, 2, 3, 4, 5]

y = [100, 200, 300, 400, 500]

plt.plot(
    x,
    y,
    marker="o"
)

plt.yticks(
    [100, 200, 300, 400, 500]
)

plt.title("Custom Y-Axis Ticks")

plt.show()


# .........................Custom Tick Labels.........................#

x = [1, 2, 3, 4, 5]

y = [10, 20, 30, 40, 50]

plt.plot(
    x,
    y,
    marker="o"
)

plt.xticks(
    [1, 2, 3, 4, 5],
    ["A", "B", "C", "D", "E"]
)

plt.title("Custom X-Axis Labels")

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

plt.yticks(
    [0, 20, 40, 60, 80, 100]
)

plt.title("Student Marks")

plt.xlabel("Students")

plt.ylabel("Marks")

plt.show()


# .........................Tick Rotation.........................#

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June"
]

sales = [
    20000,
    25000,
    30000,
    28000,
    35000,
    40000
]

plt.bar(
    months,
    sales
)

plt.xticks(
    rotation=45
)

plt.title("Monthly Sales")

plt.xlabel("Month")

plt.ylabel("Sales")

plt.show()


# .........................Tick Font Size.........................#

x = [1, 2, 3, 4, 5]

y = [10, 20, 15, 30, 25]

plt.plot(
    x,
    y,
    marker="o"
)

plt.xticks(
    fontsize=12
)

plt.yticks(
    fontsize=12
)

plt.title("Tick Font Size")

plt.show()


# .........................Tick Rotation and Font Size.........................#

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
    35000,
    40000
]

plt.plot(
    months,
    sales,
    marker="o"
)

plt.xticks(
    rotation=45,
    fontsize=10
)

plt.yticks(
    fontsize=10
)

plt.title("Sales Trend")

plt.xlabel("Month")

plt.ylabel("Sales")

plt.grid()

plt.show()


# .........................Removing Ticks.........................#

x = [1, 2, 3, 4, 5]

y = [10, 20, 15, 30, 25]

plt.plot(
    x,
    y,
    marker="o"
)

plt.xticks([])

plt.yticks([])

plt.title("Without Axis Ticks")

plt.show()


# .........................Setting Tick Range.........................#

x = [0, 10, 20, 30, 40, 50]

y = [5, 15, 25, 35, 45, 55]

plt.plot(
    x,
    y,
    marker="o"
)

plt.xticks(
    [0, 10, 20, 30, 40, 50]
)

plt.yticks(
    [0, 10, 20, 30, 40, 50, 60]
)

plt.title("Tick Range")

plt.show()


# .........................Scatter Plot with Ticks.........................#

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

plt.xticks(
    [1, 2, 3, 4, 5, 6]
)

plt.yticks(
    [40, 50, 60, 70, 80, 90]
)

plt.title("Study Hours and Marks")

plt.xlabel("Study Hours")

plt.ylabel("Marks")

plt.grid()

plt.show()


# .........................Important Functions.........................#

# plt.xticks()
#       -> Controls X-axis tick positions and labels
#
# Example:
#
# plt.xticks(
#     [1, 2, 3, 4, 5]
# )


# plt.yticks()
#       -> Controls Y-axis tick positions and labels
#
# Example:
#
# plt.yticks(
#     [0, 20, 40, 60, 80, 100]
# )


# .........................Custom Tick Labels.........................#

# plt.xticks(
#     [1, 2, 3],
#     ["A", "B", "C"]
# )
#
# First list
#       -> Tick positions
#
# Second list
#       -> Tick labels


# .........................Tick Rotation.........................#

# plt.xticks(
#     rotation=45
# )
#
#       -> Rotates X-axis labels


# .........................Tick Font Size.........................#

# plt.xticks(
#     fontsize=12
# )
#
# plt.yticks(
#     fontsize=12
# )
#
#       -> Changes tick label size


# .........................Removing Ticks.........................#

# plt.xticks([])
#
# plt.yticks([])
#
#       -> Removes axis ticks


# .........................Important Syntax.........................#

# plt.xticks(
#     positions,
#     labels,
#     rotation=45,
#     fontsize=12
# )
#
# plt.yticks(
#     positions,
#     fontsize=12
# )
#
# plt.show()
```
