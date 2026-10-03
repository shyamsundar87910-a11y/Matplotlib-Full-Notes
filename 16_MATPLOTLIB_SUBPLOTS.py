```python id="7z9j4w"
# ===================== 16_MATPLOTLIB_SUBPLOTS.py =====================


import matplotlib.pyplot as plt


# .........................Simple Subplot.........................#

plt.subplot(
    1,
    2,
    1
)

plt.plot(
    [1, 2, 3, 4, 5],
    [10, 20, 15, 30, 25]
)

plt.title("Line Plot")


plt.subplot(
    1,
    2,
    2
)

plt.bar(
    ["A", "B", "C", "D"],
    [20, 30, 25, 40]
)

plt.title("Bar Chart")

plt.show()


# .........................Two Rows Subplots.........................#

plt.subplot(
    2,
    1,
    1
)

plt.plot(
    [1, 2, 3, 4, 5],
    [10, 20, 15, 30, 25]
)

plt.title("Sales")


plt.subplot(
    2,
    1,
    2
)

plt.plot(
    [1, 2, 3, 4, 5],
    [15, 25, 20, 35, 30]
)

plt.title("Expenses")

plt.show()


# .........................Four Subplots.........................#

plt.subplot(
    2,
    2,
    1
)

plt.plot(
    [1, 2, 3, 4],
    [10, 20, 15, 25]
)

plt.title("Line")


plt.subplot(
    2,
    2,
    2
)

plt.bar(
    ["A", "B", "C"],
    [20, 30, 25]
)

plt.title("Bar")


plt.subplot(
    2,
    2,
    3
)

plt.scatter(
    [1, 2, 3, 4],
    [15, 25, 20, 30]
)

plt.title("Scatter")


plt.subplot(
    2,
    2,
    4
)

plt.hist(
    [45, 50, 55, 60, 65, 70, 75, 80],
    bins=4
)

plt.title("Histogram")

plt.show()


# .........................Subplots with Labels.........................#

plt.subplot(
    1,
    2,
    1
)

months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr"
]

sales = [
    20000,
    25000,
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


plt.subplot(
    1,
    2,
    2
)

expenses = [
    15000,
    18000,
    22000,
    25000
]

plt.plot(
    months,
    expenses
)

plt.title("Monthly Expenses")

plt.xlabel("Month")

plt.ylabel("Expenses")

plt.show()


# .........................Subplots with Figure Size.........................#

plt.figure(
    figsize=(10, 5)
)

plt.subplot(
    1,
    2,
    1
)

plt.plot(
    [1, 2, 3, 4, 5],
    [10, 20, 15, 30, 25]
)

plt.title("Line Plot")


plt.subplot(
    1,
    2,
    2
)

plt.bar(
    ["A", "B", "C", "D"],
    [20, 30, 25, 40]
)

plt.title("Bar Chart")

plt.show()


# .........................Sales Dashboard Example.........................#

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


plt.subplot(
    2,
    2,
    1
)

plt.plot(
    months,
    sales,
    marker="o"
)

plt.title("Sales")

plt.grid()


plt.subplot(
    2,
    2,
    2
)

plt.plot(
    months,
    expenses,
    marker="o"
)

plt.title("Expenses")

plt.grid()


plt.subplot(
    2,
    2,
    3
)

plt.bar(
    months,
    sales
)

plt.title("Sales Bar Chart")


plt.subplot(
    2,
    2,
    4
)

plt.scatter(
    sales,
    expenses
)

plt.title("Sales vs Expenses")

plt.grid()

plt.show()


# .........................Student Performance Dashboard.........................#

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

attendance = [
    80,
    85,
    95,
    75,
    90
]


plt.figure(
    figsize=(10, 6)
)


plt.subplot(
    2,
    2,
    1
)

plt.bar(
    students,
    marks
)

plt.title("Student Marks")

plt.xticks(
    rotation=45
)


plt.subplot(
    2,
    2,
    2
)

plt.bar(
    students,
    attendance
)

plt.title("Attendance")

plt.xticks(
    rotation=45
)


plt.subplot(
    2,
    2,
    3
)

plt.scatter(
    attendance,
    marks
)

plt.title("Attendance vs Marks")

plt.xlabel("Attendance")

plt.ylabel("Marks")

plt.grid()


plt.subplot(
    2,
    2,
    4
)

plt.plot(
    students,
    marks,
    marker="o"
)

plt.title("Marks Trend")

plt.xticks(
    rotation=45
)

plt.grid()

plt.show()


# .........................Using plt.tight_layout.........................#

plt.subplot(
    2,
    2,
    1
)

plt.plot(
    [1, 2, 3, 4],
    [10, 20, 15, 30]
)

plt.title("Line")


plt.subplot(
    2,
    2,
    2
)

plt.bar(
    ["A", "B", "C"],
    [20, 30, 25]
)

plt.title("Bar")


plt.subplot(
    2,
    2,
    3
)

plt.scatter(
    [1, 2, 3, 4],
    [15, 25, 20, 30]
)

plt.title("Scatter")


plt.subplot(
    2,
    2,
    4
)

plt.hist(
    [45, 50, 60, 70, 80, 90],
    bins=3
)

plt.title("Histogram")


plt.tight_layout()

plt.show()


# .........................Important Functions.........................#

# plt.subplot(rows, columns, position)
#       -> Creates a subplot
#
# rows
#       -> Number of rows
#
# columns
#       -> Number of columns
#
# position
#       -> Position of the current plot
#
```
